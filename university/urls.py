from django.urls import path
from . import views

urlpatterns = [
    #대학 CRU
    path('', views.UniversityLV.as_view(), name='university_list'),
    path('add/', views.UniversityCV.as_view(), name='university_add'),
    path('<int:pk>/update/', views.UniversityUV.as_view(), name='university_update'),

    #대학 데이터 CRU (이수구분, 영역, 트랙)
    path('data/', views.UniversityDataLV.as_view(), name='university_data_list'),
    path('data/<int:pk>/', views.UniversityDataDV.as_view(), name='university_data_detail'),

    #학과 데이터 CRU
    path('department/', views.DepartmentUniversityLV.as_view(), name='department_university_list'),
    path('department/<int:university>/', views.DepartmentLV.as_view(), name='department_list'),
    path('department/<int:university>/add/', views.DepartmentCV.as_view(), name='department_add'),
    path('department/<int:university>/<int:pk>/update/', views.DepartmentUV.as_view(), name='department_update'),

    #커뮤니티 그룹
    path('community/', views.CommunityLV.as_view(), name='community_list'),
]