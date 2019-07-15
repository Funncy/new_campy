from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from student.models import StudentInfo
from student.mixin import DefaultMixin, StaffRequiredMixin
from .models import University, CompletionDivision, Area, Track, \
    Department, Community
from .serializers import DepartmentSerializer, UniversitySerializer
from .forms import UniversityForm, DepartmentForm

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
    form_class = UniversityForm
    active = 'universityActive'
    success_url = '/university/'

class UniversityUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = University
    template_name = 'university_form.html'
    form_class = UniversityForm
    active = 'universityActive'
    success_url = '/university/'

class UniversityDeleteV(DefaultMixin, StaffRequiredMixin, DeleteView):
    model = University
    active = 'universityActive'
    success_url = '/university/'

    # get 막기 ( API처럼 사용 )
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

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
    form_class = DepartmentForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 저장할때 대학 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        self.object.university_id = self.kwargs['university']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('department_list', args=(self.object.university_id, ))

class DepartmentUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = Department
    template_name = 'department_form.html'
    active = 'departmentActive'
    form_class = DepartmentForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 저장할때 대학 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        self.object.university_id = self.kwargs['university']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('department_list', args=(self.object.university_id,))

class DepartmentDeleteV(DefaultMixin, StaffRequiredMixin, DeleteView):
    model = Department

    # get 막기 ( API처럼 사용 )
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('department_list', args=(self.object.university_id,))

'''
커뮤니티 그룹
'''

class CommunityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Community
    template_name = 'community_list.html'
    active = 'communityGroupActive'


'''

api 

'''

class APIDepartmentModelViewset(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return Department.objects.filter(university=university)

class UniversityGradeViewset(ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (IsAuthenticated, )