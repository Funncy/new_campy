from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'department', views.DepartmentViewset)
router.register(r'university', views.UniversityGradeViewset)
router.register(r'community', views.CommunityViewset)
router.register(r'division', views.DivisionViewset)
router.register(r'area', views.AreaViewset)
router.register(r'track', views.TrackViewset)

urlpatterns = [
    #대학 CRU
    path('', views.UniversityLV.as_view(),
         name='university_list'),
    path('add/', views.UniversityCV.as_view(),
         name='university_add'),
    path('<int:pk>/update/', views.UniversityUV.as_view(),
         name='university_update'),
    path('<int:pk>/delete/', views.UniversityDeleteV.as_view(),
         name='university_delete'),

    #대학 데이터 CRU (이수구분, 영역, 트랙)
    path('data/', views.UniversityDataLV.as_view(),
         name='university_data_list'),
    path('data/<int:pk>/', views.UniversityDataDV.as_view(),
         name='university_data_detail'),

    #학과 데이터 CRU
    path('department/', views.DepartmentUniversityLV.as_view(),
         name='department_university_list'),
    path('department/<int:university>/', views.DepartmentLV.as_view(),
         name='department_list'),
    path('department/<int:university>/add/', views.DepartmentCV.as_view(),
         name='department_add'),
    path('department/<int:university>/<int:pk>/update/', views.DepartmentUV.as_view(),
         name='department_update'),
    path('department/<int:university>/<int:pk>/delete/', views.DepartmentDeleteV.as_view(),
         name='department_delete'),

    #커뮤니티 그룹
    path('community/', views.CommunityLV.as_view(),
         name='community_list'),

    #API
    path('api/', include(router.urls)),
]