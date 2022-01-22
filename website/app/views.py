from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {})

def tool(request):
    context = {
        'patterns': ['checkered', 'dots', 'floral', 'solid', 'stripes', 'zigzag'], 
        'items': ['top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    }
    return render(request, 'tool.html', context)

def about(request):
    return render(request, 'about.html', {})