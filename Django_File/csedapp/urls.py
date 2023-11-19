from django.contrib import admin
from django.urls import path, include
from csedapp import views

urlpatterns = [
    path("", views.index, name= 'home'),
    path("about", views.about, name= 'about'),
    # path("get_data", views.get_data, name='get_data'),
    path("lol", views.lol, name= 'lol'),
    path("contact", views.contact, name= 'contact'),
]