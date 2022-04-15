from django.urls import path
from parts import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('main', views.main, name='main'),
    path('about', views.about, name='about'),
    # path('download_parts', views.download_parts, name='download_parts'),
]