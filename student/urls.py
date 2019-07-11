from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.JoinLV.as_view(), name='join'),
    path('mypage/', views.MypageLV.as_view(), name='mypage'),
]