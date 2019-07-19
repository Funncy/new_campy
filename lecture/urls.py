from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'subject', views.SubjectReadViewset)
router.register(r'lecture', views.LectureReadViewset)

urlpatterns = [
    # UI
    path('<int:university>/', views.LectureLV.as_view(), name='lecture_list'),
    path('upload/', views.LectureUploadFV.as_view(), name='lecture_upload'),
    path('subject/<int:university>/<int:division>/<int:area>/',
         views.SubjectLV.as_view(), name='subject_list'),

    # API
    path('api/', include(router.urls)),
]