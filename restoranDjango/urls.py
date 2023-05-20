"""
URL configuration for restoranDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import index, main, menu, salads, second, breakfest, zakuski, sweets, rezerv, third, menu2

urlpatterns = [
    path('', index, name='index'),
    path('main/', main, name='main'),
    path('menu/', menu, name='menu'),
    path('menu2/', menu2, name='menu2'),
    path('salads/', salads, name='salads'),
    path('second/', second, name='second'),
    path('breakfest/', breakfest, name='breakfest'),
    path('zakuski/', zakuski, name='zakuski'),
    path('sweets/', sweets, name='sweets'),
    path('rezerv/', rezerv, name='rezerv'),
    path('third/', third, name='third'),
]
