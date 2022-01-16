from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tool', views.tool, name='tool'),
    path('about', views.about, name='about'),
]