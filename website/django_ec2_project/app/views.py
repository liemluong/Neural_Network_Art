from distutils.command.upload import upload
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import *
from .generator import *

def home(request):
    return render(request, 'home.html', {})

@csrf_exempt
def generator(request):
    # create a form instance and populate it with data from the request:
    pattern_form = PatternGeneratorForm(request.POST, request.FILES)
    download_form = DownloadForm(request.POST)
    print(download_form.is_valid())
    print(pattern_form.is_valid())
    print(download_form.errors)
    # upload_form = UploadForm(request.POST, request.FILES, use_required_attribute=False)
    if request.method == 'POST':
        if download_form.is_valid():
            pattern_form = PatternGeneratorForm()
            file_type = request.POST.get('file_type')
            content = request.POST.get('content')
            width = int(request.POST.get('width'))
            height = int(request.POST.get('height'))
            pattern = request.POST.get('pattern')
            if content == 'pattern':
                image = Image.open('../django_ec2_project/static/patterns/{}.jpg'.format(pattern))
                if file_type == 'PNG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.png')
                if file_type == 'JPG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.jpg')
            elif content == 'item':
                image = Image.open('../django_ec2_project/static/outputs/display_image.jpg')
                if file_type == 'PNG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.png')
                if file_type == 'JPG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.jpg')
        else:
            download_form = DownloadForm()
            if pattern_form.is_valid():
                pattern_form.save()
                use_upload = json.loads(request.POST.get('use_upload'))
                pattern = request.POST.get('pattern')
                if use_upload:
                    item = request.FILES['item_image'].name
                    obj_img = load_image(item, 'upload')
                else:
                    item = request.POST.get('item')
                    selected_object_image = '{}.png'.format(item)
                    obj_img = load_image(selected_object_image, 'obj')

                # User selects object and style from the web
                # The two images are loaded into the model
                selected_style_image = '{}.jpg'.format(pattern)

                # Call function to load image
                stl_img = load_image(selected_style_image, 'stl')

                # Call function to resize the style image to match with the shape of the object image
                stl_img = resize_image(obj_img, stl_img)

                # Call function to predict and generate the masking layer from an object image
                contour_image = mask_image(obj_img, stl_img)

                # Call function to blend the object image with style image on top of masking layer
                transform_image(obj_img, contour_image, stl_img)
                save_image(obj_img, 'display_image')
            else:
                print('not valid')
                pattern_form = PatternGeneratorForm()

    context = {
        'patterns': ['cartoon', 'checkered', 'cheetah', 'dots', 'floral', 'leaves', 'solid', 'stripes', 'zigzag'],
        'items': ['bag', 'boots', 'coat', 'dress', 'pants', 'sandals', 'shirt', 'shoes', 'sweater'],
        'generator_form': pattern_form,
        'download_form': download_form,
    }

    return render(request, 'generator.html', context)


def about_team(request):
    return render(request, 'about_team.html', {})

def about_nn(request):
    return render(request, 'about_nn.html', {})

def about_project(request):
    return render(request, 'about_project.html', {})