from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ScheduleLV.as_view(), name='schedule_list'),
    path('add/', views.ScheduleCV.as_view(), name='schedule_add'),
    path('<int:pk>/update/', views.ScheduleUV.as_view(), name='schedule_update'),
]