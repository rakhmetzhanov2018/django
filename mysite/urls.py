"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf45
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  pathooi']\
"""
from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path('', views.empty),
    path('main_screen/', include('polls.urls')),
    path('main_screen/historyQ/', views.his),
    path('admin/', admin.site.urls),
    path('main_screen/historyQ/hq1/', views.hq1),
    path('main_screen/historyQ/hq2/', views.hq2),
    path('main_screen/historyQ/hq3/', views.hq3),
    path('main_screen/geometryQ/', views.his),
    path('main_screen/geometryQ/gq1', views.gq1),
    path('main_screen/geometryQ/gq2', views.gq2),
    path('main_screen/geometryQ/gq3', views.gq3),
]
