from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from student.mixin import LoginRequiredMixin, DefaultMixin, StaffRequiredMixin
from university.models import University
from .models import SubjectGroup, RuleGeneral, RuleSpecific
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
졸업진단을 위한 과목그룹 UI
'''
class SubjectGroupLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = SubjectGroup
    template_name = 'subject_group_list.html'
    active = 'subjectGroupActive'

class SubjectGroupCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = SubjectGroup
    template_name = 'subject_group_form.html'
    fields = ('completion_divisions', 'name')
    active = 'subjectGroupActive'
    success_url = ''

class SubjectGroupUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = SubjectGroup
    template_name = 'subject_group_form.html'
    fields = ('completion_divisions', 'name')
    active = 'subjectGroupActive'
    success_url = ''

'''
졸업진단을 위한 룰 UI
'''
class RuleUniversityLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = University
    template_name = 'rule_university_list.html'
    active = 'ruleActive'

class RuleGeneralLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = RuleGeneral
    template_name = 'rule_general_list.html'
    active = 'ruleActive'

class RuleGeneralCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = RuleGeneral
    template_name = 'rule_general_form.html'
    active = 'ruleActive'
    fields = ('name', 'track', 'type', 'value', 'subject_group')

class RuleGeneralUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = RuleGeneral
    template_name = 'rule_general_form.html'
    active = 'ruleActive'
    fields = ('name', 'track', 'type', 'value', 'subject_group')


class RuleSpecificLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = RuleSpecific
    template_name = 'rule_specific_list.html'
    active = 'ruleActive'


class RuleSpecificCV(DefaultMixin, StaffRequiredMixin, CreateView):
    model = RuleSpecific
    template_name = 'rule_specific_form.html'
    active = 'ruleActive'
    fields = ('name', 'track', 'type', 'value', 'subject_group', 'upper_rule')


class RuleSpecificUV(DefaultMixin, StaffRequiredMixin, UpdateView):
    model = RuleSpecific
    template_name = 'rule_specific_form.html'
    active = 'ruleActive'
    fields = ('name', 'track', 'type', 'value', 'subject_group', 'upper_rule')


