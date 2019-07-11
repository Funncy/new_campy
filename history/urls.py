from django.urls import path
from . import views

urlpatterns = [
    path('lecture/', views.LectureHistoryLV.as_view(), name='lecture_history'),
]