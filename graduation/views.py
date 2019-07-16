from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from student.mixin import LoginRequiredMixin, DefaultMixin, StaffRequiredMixin
from university.models import University, Track, Department
from university.mixin import UniversityMixin
from student.models import StudentInfo
from .models import SubjectGroup, RuleGeneral, RuleSpecific
from .forms import SubjectGroupForm, RuleGeneralForm, RuleSpecificForm
# Create your views here.

'''
졸업 판정 결과
'''
class GraduationDiagnosisTV(DefaultMixin, LoginRequiredMixin, TemplateView):
    template_name = 'graduation_diagnosis.html'
    active = 'graduationDiagnosisActive'

    #졸업 판정 진행결과 넣기
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = None
        return context

'''
졸업진단을 위한 과목그룹 UI List Create Update Delete
'''
class SubjectGroupLV(DefaultMixin, StaffRequiredMixin, UniversityMixin, ListView):
    model = SubjectGroup
    template_name = 'subject_group_list.html'
    active = 'subjectGroupActive'
    paginate_by = 10

    def get_queryset(self):
        return SubjectGroup.objects.filter(university=self.kwargs['university'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = self.kwargs['university']
        return context

class SubjectGroupCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = SubjectGroup
    template_name = 'subject_group_form.html'
    form_class = SubjectGroupForm
    active = 'subjectGroupActive'

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        return context

    # 저장할때 대학 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.save()
        # Many To Many Fields Save
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('subject_group_list', args=(self.object.university_id, ))

class SubjectGroupUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = SubjectGroup
    template_name = 'subject_group_form.html'
    form_class = SubjectGroupForm
    active = 'subjectGroupActive'

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        return context

    # 저장할때 대학 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.save()
        # Many To Many Fields Save
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('subject_group_list', args=(self.object.university_id, ))

class SubjectGroupDV(DefaultMixin, StaffRequiredMixin, DeleteView):
    model = SubjectGroup

    # get 막기 ( API처럼 사용 )
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('subject_group_list', args=(self.object.university_id,))

'''
졸업진단을 위한 공통 룰 UI List Create Update Delete
'''
class RuleUniversityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = University
    template_name = 'rule_university_list.html'
    active = 'ruleActive'

class RuleGeneralLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = RuleGeneral
    template_name = 'rule_general_list.html'
    active = 'ruleActive'

    def get_queryset(self):
        return RuleGeneral.objects.filter(university=self.kwargs['university'],\
                                          track=self.kwargs['track'],\
                                          year=self.kwargs['year'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Track 추가 해당 대학에 맞춰서
        context['tracks'] = Track.objects.filter(university_id=self.kwargs['university'])
        # year 추가 '없음' 넣기
        context['years'] = list()
        context['years'].append(('0', '전체'))
        context['years'] += [(x,x) for x in reversed(range(1950, 2021))]
        # 대학,년도,트랙 정보 넣기 Search용
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_year'] = self.kwargs['year']
        context['current_track'] = self.kwargs['track']
        return context


class RuleGeneralCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = RuleGeneral
    template_name = 'rule_general_form.html'
    active = 'ruleActive'
    form_class = RuleGeneralForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_year'] = self.kwargs['year']
        return context

    # 저장할때 대학,년도 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.year = self.kwargs['year']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('rule_general_list', args=(self.object.university_id, self.object.year, 1 ))

class RuleGeneralUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = RuleGeneral
    template_name = 'rule_general_form.html'
    active = 'ruleActive'
    form_class = RuleGeneralForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_year'] = self.kwargs['year']
        return context

    # 저장할때 대학,년도 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.year = self.kwargs['year']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('rule_general_list', args=(self.object.university_id, self.object.year, 1))

class RuleGeneralDV(DefaultMixin, StaffRequiredMixin, DeleteView):
    model = RuleGeneral

    # get 막기 ( API처럼 사용 )
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('rule_general_list', args=(self.object.university_id, self.object.year, 1))


'''
 졸업진단을 위한 특정 룰 UI List Create Update Delete
'''

class RuleSpecificLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = RuleSpecific
    template_name = 'rule_specific_list.html'
    active = 'ruleActive'

    def get_queryset(self):
        return RuleSpecific.objects.filter(university=self.kwargs['university'],\
                                           department=self.kwargs['department'],\
                                          track=self.kwargs['track'],\
                                          year=self.kwargs['year'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Track 추가 해당 대학에 맞춰서
        context['tracks'] = Track.objects.filter(university_id=self.kwargs['university'])
        # year 추가
        context['years'] = [(x,x) for x in reversed(range(1950, 2021))]
        # Department 추가
        context['departments'] = Department.objects.filter(university=self.kwargs['university'])
        # 대학,년도,트랙 정보 넣기 Search용
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_department'] = Department.objects.get(pk=self.kwargs['department'])
        context['current_year'] = self.kwargs['year']
        context['current_track'] = self.kwargs['track']
        return context


class RuleSpecificCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = RuleSpecific
    template_name = 'rule_specific_form.html'
    active = 'ruleActive'
    form_class = RuleSpecificForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        kwargs['year'] = self.kwargs['year']
        kwargs['department'] = Department.objects.get(pk=self.kwargs['department'])
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_department'] = Department.objects.get(pk=self.kwargs['department'])
        context['current_year'] = self.kwargs['year']
        return context

    # 저장할때 대학,년도 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.year = self.kwargs['year']
        self.object.department_id = self.kwargs['department']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('rule_specific_list', args=(self.object.university_id, self.object.year,
                                                   self.object.department_id, 1))


class RuleSpecificUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = RuleSpecific
    template_name = 'rule_specific_form.html'
    active = 'ruleActive'
    form_class = RuleSpecificForm

    # Form에 대학 정보 넣어주기 위함
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['university'] = StudentInfo.objects.get(user_id=self.request.user.id).university_id
        kwargs['year'] = self.kwargs['year']
        kwargs['department'] = Department.objects.get(pk=self.kwargs['department'])
        return kwargs

    # 화면에 대학정보 뿌려주기 위함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_university'] = University.objects.get(pk=self.kwargs['university'])
        context['current_department'] = Department.objects.get(pk=self.kwargs['department'])
        context['current_year'] = self.kwargs['year']
        return context

    # 저장할때 대학,년도 정보 추가
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 대학정보 추가
        self.object.university_id = self.kwargs['university']
        self.object.year = self.kwargs['year']
        self.object.department_id = self.kwargs['department']
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('rule_specific_list', args=(self.object.university_id, self.object.year,
                                                   self.object.department_id, 1))

class RuleSpecificDV(DefaultMixin, StaffRequiredMixin, DeleteView):
    model = RuleSpecific

    # get 막기 ( API처럼 사용 )
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('rule_specific_list', args=(self.object.university_id, self.object.year,
                                                   self.object.department_id, 1))




