from turtle import update
from unicodedata import name
from django.urls import path
from social import views

urlpatterns= [
    path('',views.index)
 ]
from django.contrib import admin
from django.urls import path
from social import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('Home',views.Home,name="home"),
    path('profile',views.profile,name="profile"),
    path('logout',views.signout,name='logout'),
    path('register',views.register,name='register'),
    path('update',views.update_profile,name='update'),
    path('addpost',views.create_post,name='addpost')
]