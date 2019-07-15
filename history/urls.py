from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'history', views.LectureHistoryListViewset)

urlpatterns = [
    # UI
    path('lecture/', views.LectureHistoryLV.as_view(), name='lecture_history'),

    # API
    path('api/', include(router.urls)),
]