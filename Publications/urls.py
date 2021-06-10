from django.contrib import admin
from django.urls import path, include
from Publications import views

urlpatterns = [
    path('', views.index, name='home'),
    path('publications', views.publications, name='publications'),
    path('contact', views.contact, name='contact')
]