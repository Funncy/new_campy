from django.urls import path
from . import views

urlpatterns = [
    path('', views.GraduationDiagnosisTV.as_view(), name='graduation_diagnosis'),
]