from distutils.command.upload import upload
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import *
from .generator import *

def home(request):
    '''
    Render home page
    '''
    return render(request, 'home.html', {})

@csrf_exempt
def generator(request):
    '''
    Render generator
    Handles POST requests for pattern generator and download forms
    '''
    # create a form instance and populate it with data from the request:
    pattern_form = PatternGeneratorForm(request.POST, request.FILES)
    download_form = DownloadForm(request.POST)
    if request.method == 'POST':
        # Handle download form
        if download_form.is_valid():
            pattern_form = PatternGeneratorForm()
            file_type = request.POST.get('file_type')
            content = request.POST.get('content')
            width = int(request.POST.get('width'))
            height = int(request.POST.get('height'))
            pattern = request.POST.get('pattern')
            # If downloading pattern, grab presaved pattern at ../django_ec2_project/static/outputs/download.jpg 
            # and resize to user specifications
            if content == 'pattern':
                image = Image.open('../django_ec2_project/static/outputs/download.jpg')
                if file_type == 'PNG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.png')
                if file_type == 'JPG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.jpg')
            # If downloading item, grab presaved item at ../django_ec2_project/static/outputs/display_image.jpg, 
            # resize to user specifications and resave as download.jpg/png
            elif content == 'item':
                image = Image.open('../django_ec2_project/static/outputs/display_image.jpg')
                if file_type == 'PNG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.png')
                if file_type == 'JPG':
                    resized_image = image.resize((width, height))
                    resized_image.save('../django_ec2_project/static/outputs/download.jpg')
        # Handle pattern generation
        else:
            download_form = DownloadForm()
            if pattern_form.is_valid():
                pattern_form.save()
                use_upload = json.loads(request.POST.get('use_upload'))
                pattern = request.POST.get('pattern')
                # Load user uploaded image or item
                if use_upload:
                    item = request.FILES['item_image'].name
                    obj_img = load_image(item, 'upload')
                else:
                    item = request.POST.get('item')
                    selected_object_image = '{}.png'.format(item)
                    obj_img = load_image(selected_object_image, 'obj')

                # Load random version of user selected pattern into the model
                selected_style_image = '{}'.format(pattern)

                # Call function to load pattern
                stl_img = load_image(selected_style_image, 'stl')

                # Call function to resize the pattern image to match with the shape of the item image
                stl_img = resize_image(obj_img, stl_img)

                # Call function to predict and generate the masking layer from an item image
                contour_image = mask_image(obj_img, stl_img)

                # Call function to blend the item image with pattern image on top of masking layer
                transform_image(obj_img, contour_image, stl_img)

                # Save the image
                save_image(obj_img, 'display_image')
            else:
                pattern_form = PatternGeneratorForm()

    # Send forms and form options to front end
    context = {
        'patterns': ['cartoon', 'checkered', 'cheetah', 'dots', 'floral', 'leaves', 'solid', 'stripes', 'zigzag'],
        'items': ['bag', 'boots', 'coat', 'dress', 'pants', 'sandals', 'shirt', 'shoes', 'sweater'],
        'generator_form': pattern_form,
        'download_form': download_form,
    }

    return render(request, 'generator.html', context)

def about_team(request):
    '''
    Render about team page
    '''
    return render(request, 'about_team.html', {})

def about_nn(request):
    '''
    Render about neural network page
    '''
    return render(request, 'about_nn.html', {})

def about_project(request):
    '''
    Render about project page
    '''
    return render(request, 'about_project.html', {})