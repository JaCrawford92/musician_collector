from django.urls import path
from . import views

urlpatterns = [
    # about page is the first page that will be displayed
    path('about/', views.about, name='about'),

    # the home page for the site
    path('', views.home, name='home'),

    # page for all musicians
    path('musicians/', views.musicians_index, name='index'),

    # page for a specific musician
    path('musicians/<int:musician_id>/', views.musicians_detail, name='detail'),

    # page for creating a new musician
    path('musicians/create/', views.MusicianCreate.as_view(), name='musicians_create'),

    # page for updating a musician
    path('musicians/<int:pk>/update/', views.MusicianUpdate.as_view(), name='musicians_update'),

    # page for deleting a musician
    path('musician/<int:pk>/delete/', views.MusicianDelete.as_view(), name='musicians_delete')
]