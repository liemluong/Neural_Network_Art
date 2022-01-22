from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tool', views.tool, name='tool'),
    path('about', views.about, name='about'),
]