from distutils.command.upload import upload
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import *
from .generator import *
from PIL import Image
from io import BytesIO
from django.http import HttpResponse
import base64
from django.http import JsonResponse


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
            img = request.POST.get('img')
            # If downloading pattern, grab presaved pattern at ../django_ec2_project/static/outputs/download.jpg 
            # and resize to user specifications
            if content == 'pattern':
                image = Image.open(pattern)
            # If downloading item, grab presaved item at ../django_ec2_project/static/outputs/display_image.jpg, 
            # resize to user specifications and resave as download.jpg/png
            elif content == 'item':
                image = Image.open(BytesIO(base64.b64decode(img)))
            if file_type == 'PNG':
                resized_image = image.resize((width, height))
                img_byte_arr = BytesIO()
                resized_image.save(img_byte_arr, format='PNG')
                return HttpResponse(base64.b64encode(img_byte_arr.getvalue()), "image/png")
            elif file_type == 'JPG':
                resized_image = image.resize((width, height))
                img_byte_arr = BytesIO()
                resized_image.save(img_byte_arr, format='JPEG')
                return HttpResponse(base64.b64encode(img_byte_arr.getvalue()), "image/jpeg")
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
                stl_img, random_pattern = load_image(selected_style_image, 'stl')

                # Call function to resize the pattern image to match with the shape of the item image
                stl_img = resize_image(obj_img, stl_img)

                # Call function to predict and generate the masking layer from an item image
                contour_image = mask_image(obj_img, stl_img)

                # Call function to blend the item image with pattern image on top of masking layer
                transform_image(obj_img, contour_image, stl_img)

                # Save the image
                img_byte_arr = BytesIO()
                obj_img = Image.fromarray(obj_img)
                obj_img.save(img_byte_arr, format='PNG')
                response = {'item': base64.b64encode(img_byte_arr.getvalue()).decode(), 'pattern': random_pattern}

                return JsonResponse(response)

                #save_image(obj_img, 'display_image')
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