from django.urls import path
from . import views

urlpatterns = [
    path('get_all', views.get_all),
    path('create_new', views.create_new),
    path('delete', views.delete_device),
    path('speak', views.speak),
    path('get_location', views.get_location),
]
