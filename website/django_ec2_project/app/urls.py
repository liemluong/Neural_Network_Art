from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generator', views.generator, name='generator'),
    path('about-team', views.about_team, name='about_team'),
    path('about-nn', views.about_nn, name='about_nn'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)