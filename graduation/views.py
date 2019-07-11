from django.shortcuts import render
from django.views.generic import TemplateView
from student.mixin import LoginRequiredMixin, DefaultMixin

# Create your views here.

class GraduationDiagnosisTV(DefaultMixin, LoginRequiredMixin, TemplateView):
    template_name = 'graduation_diagnosis.html'
    active =  'graduationDiagnosisActive'

    #졸업 판정 진행결과 넣기
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = None
        return context