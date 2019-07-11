from django.urls import path
from . import views

urlpatterns = [
    path('<int:university>/', views.LectureLV.as_view(), name='lecture_list'),
    path('upload/', views.LectureUploadFV, name='lecture_upload'),
    path('subject/<int:university>/<int:division>/<int:area>/',
         views.SubjectLV.as_view(), name='subject_list'),
]