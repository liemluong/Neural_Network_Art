import cv2
import os
import copy
import torch
import torchvision
import PIL.Image
import numpy as np
import albumentations as albu

import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PIL import Image
from iglovikov_helper_functions.utils.image_utils import load_rgb, pad, unpad
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
from cloths_segmentation.pre_trained_models import create_model

#####
#####


def load_image(selected_image, identifier):
    '''
    Load images
    '''
    if identifier == 'obj':
        object_image = cv2.imread(os.path.join('../django_ec2_project/static/items', selected_image))
        img = object_image[:, :, ::-1]  # convert RGB to BGR
    else:
        style_image = cv2.imread(os.path.join('../django_ec2_project/static/patterns', selected_image))
        img = style_image[:, :, ::-1]  # convert RGB to BGR

    return img


def resize_image(source_img, target_img):
    '''
    Resize the style image to the same size of the object image
    '''
    target_img = cv2.resize(target_img, (source_img.shape[1], source_img.shape[0]))

    return target_img


def mask_image(O_img, S_img):
    '''
    Generate the mask layer of the object fashion image
    '''
    # Set up the model using the Unet version
    # fail here: check this one https://github.com/ternaus/cloths_segmentation/blob/main/cloths_segmentation/pre_trained_models.py

    model = create_model("Unet_2020-10-30")
    model.eval()

    # Set up images for transformation the art image into an array type
    new_object_image = copy.deepcopy(O_img)
    new_art_image = PIL.Image.fromarray((S_img * 255).astype(np.uint8))

    transform = albu.Compose([albu.Normalize(p=1)], p=1)

    padded_image, pads = pad(new_object_image, factor=32, border=cv2.BORDER_CONSTANT)

    x = transform(image=padded_image)["image"]
    x = torch.unsqueeze(tensor_from_rgb_image(x), 0)

    with torch.no_grad():
        prediction = model(x)[0][0]

    mask = (prediction > 0).cpu().numpy().astype(np.uint8)

    mask = unpad(mask, pads)

    # Convert the mask image into a black & white image
    bw_image = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB) * 255

    return bw_image


def transform_image(original, bw, fill):
    '''
    Transformation function to blend the art into the mask contour onto the original image
    '''
    pos_ind = np.zeros((original.shape[0], original.shape[1]))
    for i in range(bw.shape[0]):
        for j in range(bw.shape[1]):
            if np.array_equal(bw[i, j], np.array([255, 255, 255])):
                pos_ind[i, j] = 1
    for i in range(original.shape[0]):
        for j in range(original.shape[1]):
            if pos_ind[i, j] == 1:
                original[i, j] = fill[i, j]


def save_image(final_image, file_name):
    '''
    Save the result of the final result into the output_images folder
    '''
    file_name = file_name + '.jpg'
    im = Image.fromarray(final_image)
    im.save(os.path.join('../django_ec2_project/static/outputs', file_name))