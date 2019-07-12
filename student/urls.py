from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.JoinCV.as_view(), name='join'),
    path('mypage/', views.MypageUV.as_view(), name='mypage'),
]