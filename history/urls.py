from django.urls import path, include
from . import views

urlpatterns = [
    path('lecture/', views.LectureHistoryLV.as_view(), name='lecture_history'),
]