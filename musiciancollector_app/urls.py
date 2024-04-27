from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('musicians/', views.musicians_index, name='index'),
]