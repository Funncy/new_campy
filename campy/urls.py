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
    path('login/', views.index, name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.index, name='logout'),

    # ui list
    path('', views.index, name='index'),
    path('test/', views.index, name='test'),
    path('history/', views.index, name='history'),
    path('course/', views.index, name='course'),
    path('graduation/', views.index, name='graduation'),
    path('community/', views.index, name='community'),
    path('mypage/', views.index, name='mypage'),
    path('join/', views.index, name='join'),
    path('rule/', views.index, name='rule'),
    path('subject/', views.index, name='subject'),
    path('subject/group/', views.index, name='subject_group'),
    path('subject/group/create', views.index, name='subject_group_create'),
    path('subject/group/update', views.index, name='subject_group_update'),
    path('general/', views.index, name='general'),
    path('general/create', views.index, name='general_create'),
    path('general/update/<int:id>/', views.index, name='general_update'),

]
