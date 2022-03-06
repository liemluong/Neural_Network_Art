from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import PatternGeneratorForm
from .forms import DownloadForm
from .generator import *

def home(request):
    return render(request, 'home.html', {})

@csrf_exempt
def generator(request):
    # create a form instance and populate it with data from the request:
    pattern_form = PatternGeneratorForm(request.POST)

    if request.method == 'POST' and pattern_form.is_valid():
        pattern = request.POST.get('pattern')
        item = request.POST.get('item')

        # User selects object and style from the web
        # The two images are loaded into the model
        selected_object_image = '{}.png'.format(item)
        selected_style_image = '{}.jpg'.format(pattern)

        # Call function to load image
        obj_img = load_image(selected_object_image, 'obj')
        stl_img = load_image(selected_style_image, 'stl')

        # Call function to resize the style image to match with the shape of the object image
        stl_img = resize_image(obj_img, stl_img)

        # Call function to predict and generate the masking layer from an object image
        contour_image = mask_image(obj_img, stl_img)

        # Call function to blend the object image with style image on top of masking layer
        transform_image(obj_img, contour_image, stl_img)
        save_image(obj_img, 'display_image')

    context = {
        'patterns': ['cartoon', 'checkered', 'cheetah', 'dots', 'floral', 'leaves', 'solid', 'stripes', 'zigzag'],
        'items': ['bag', 'boots', 'coat', 'dress', 'pants', 'sandals', 'shirt', 'shoes', 'sweater'],
        'generator_form': pattern_form,
        'download_form': DownloadForm()
    }

    return render(request, 'generator.html', context)


def about_team(request):
    return render(request, 'about_team.html', {})

def about_nn(request):
    return render(request, 'about_nn.html', {})