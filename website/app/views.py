from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})

def tool(request):
    return render(request, 'tool.html', {})

def about(request):
    return render(request, 'about.html', {})