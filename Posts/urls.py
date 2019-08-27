from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    	
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('show/', views.show, name='show'),
    path('error/', views.error, name='error'),
    
]
