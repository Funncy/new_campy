from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.JoinCV.as_view(), name='join'),
    path('mypage/', views.MypageLV.as_view(), name='mypage'),
]