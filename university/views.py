from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from student.mixin import DefaultMixin, StaffRequiredMixin
from .models import University, CompletionDivision, Area, Track, \
    Department, Community

# Create your views here.

'''
대학 CRU UI 
'''
class UniversityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = University
    template_name = 'university_list.html'
    active = 'universityActive'

class UniversityCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = University
    template_name = 'university_form.html'
    fields = ('name', 'maximum_credit')
    active = 'universityActive'
    success_url = '/university/'

class UniversityUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = University
    template_name = 'university_form.html'
    fields = ('name', 'maximum_credit')
    active = 'universityActive'
    success_url = '/university/'

'''
대학정보 (이수구분, 영역, 트랙) CRU UI
'''

class UniversityDataLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = University
    template_name = 'university_data_list.html'
    active = 'universityDataActive'

    #정보 갯수 넘기기
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UniversityDataDV(DefaultMixin, StaffRequiredMixin, DetailView):
    model = University
    template_name = 'university_data_detail.html'
    active = 'universityDataActive'

    #정보 넘기기
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

'''
학과 데이터 CRU UI
'''

class DepartmentUniversityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = University
    template_name = 'department_university_list.html'
    active = 'departmentActive'

class DepartmentLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Department
    template_name = 'department_list.html'
    active = 'departmentActive'

    def get_queryset(self):
        return Department.objects.filter(university=self.kwargs['university'])

class DepartmentCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = Department
    template_name = 'department_form.html'
    active = 'departmentActive'
    fields = ('university', 'name', 'college_name', 'same_department', 'community')
    success_url = ''

class DepartmentUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = Department
    template_name = 'department_form.html'
    active = 'departmentActive'
    fields = ('university', 'name', 'college_name', 'same_department', 'community')
    success_url = ''


'''
커뮤니티 그룹
'''

class CommunityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Community
    template_name = 'community_list.html'
    active = 'communityGroupActive'
