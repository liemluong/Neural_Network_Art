from django.shortcuts import render
from .forms import PatternGeneratorForm
from .forms import DownloadForm

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {})

def generator(request):
    context = {
        'patterns': ['checkered', 'dots', 'floral', 'solid', 'stripes', 'zigzag'], 
        'items': ['top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot'],
        'generator_form': PatternGeneratorForm(),
        'download_form': DownloadForm()
    }
    return render(request, 'generator.html', context)

def about_team(request):
    return render(request, 'about_team.html', {})

def about_nn(request):
    return render(request, 'about_nn.html', {})