from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.user_login,name='login'), 
    path('add_student/',views.add_student,name='add_student'),
    #path('logout/',views.user_logout,name='logout'),
]