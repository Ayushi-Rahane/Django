from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about_page', views.about_page, name="about_page"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    
    ]
