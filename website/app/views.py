from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {})

def tool(request):
    return render(request, 'tool.html', {})

def about(request):
    return render(request, 'about.html', {})