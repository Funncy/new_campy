"""campy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    # admin list
    path('admin/', admin.site.urls),
    path('login/', views.LoginTV.as_view(), name='login'),
    path('accounts/', include('allauth.urls')),

    # ui list
    path('', views.IndexTV.as_view(), name='index'),
    path('test/', views.test, name='test'),

    # app ui list
    path('student/', include('student.urls')),
    path('history/', include('history.urls')),

]
