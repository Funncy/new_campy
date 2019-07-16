from django.urls import path
from . import views

urlpatterns = [
    #졸업진단 결과 화면
    path('', views.GraduationDiagnosisTV.as_view(), name='graduation_diagnosis'),

    #졸업진단을 위한 과목그룹 UI
    path('subject/group/<int:university>/',
         views.SubjectGroupLV.as_view(), name='subject_group_list'),
    path('subject/group/<int:university>/add/',
         views.SubjectGroupCV.as_view(), name='subject_group_add'),
    path('subject/group/<int:university>/<int:pk>/update/',
         views.SubjectGroupUV.as_view(), name='subject_group_update'),
    path('subject/group/<int:university>/<int:pk>/delete/',
         views.SubjectGroupDV.as_view(), name='subject_group_delete'),

    #졸업진단을 위한 룰 UI
    path('rule/university/', views.RuleUniversityLV.as_view(),
         name='rule_university_list'),

    path('rule/university/general/<int:university>/<int:year>/<int:track>/',
         views.RuleGeneralLV.as_view(), name='rule_general_list'),
    path('rule/university/general/<int:university>/<int:year>/add/',
         views.RuleGeneralCV.as_view(), name='rule_general_add'),
    path('rule/university/general/<int:university>/<int:year>/<int:pk>/update/',
         views.RuleGeneralUV.as_view(), name='rule_general_update'),
    path('rule/university/general/<int:university>/<int:year>/<int:pk>/delete/',
         views.RuleGeneralDV.as_view(), name='rule_general_delete'),


    path('rule/university/specific/<int:university>/<int:year>/<int:department>/<int:track>/',
         views.RuleSpecificLV.as_view(), name='rule_specific_list'),
    path('rule/university/specific/<int:university>/<int:year>/<int:department>/add/',
         views.RuleSpecificCV.as_view(), name='rule_specific_add'),
    path('rule/university/specific/<int:university>/<int:year>/<int:department>/<int:pk>/update/',
         views.RuleSpecificUV.as_view(), name='rule_specific_update'),
    path('rule/university/specific/<int:university>/<int:year>/<int:department>/<int:pk>/delete/',
         views.RuleSpecificDV.as_view(), name='rule_specific_delete'),
]