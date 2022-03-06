from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generator', views.generator, name='generator'),
    path('about-team', views.about_team, name='about_team'),
    path('about-nn', views.about_nn, name='about_nn'),
    path('about-project', views.about_project, name='about_project'),

]