"""
URL configuration for ListView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Here dealing objects that's why we are using Static URL Mapping
    path('SchoolList/',SchoolList.as_view(),name='SchoolList'),#Static URL Mapping
    path('Home/',Home.as_view(),name='Home'),#Static URL Mapping
    path('SchoolCreate/',SchoolCreate.as_view(),name='SchoolCreate'),#Static URL Mapping
    path('wish/<n>/',wish,name='wish'),

    #Here dealing with particular object that's why we are using Dynamic URL Mapping
    re_path('^update/(?P<pk>\d+)/',SchoolUpdate.as_view(),name='SchoolUpdate'),#Dynamic URL Mapping(Select Model Instance)
    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='detail'),#Dynamic URL Mapping(Select Model Instance)
]
