from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from university.models import University
from student.models import StudentInfo
from .mixin import DefaultMixin, LoginRequiredMixin
from university.mixin import UniversityMixin
from .forms import StudentForm
# Create your views here.

class JoinCV(DefaultMixin, LoginRequiredMixin, UniversityMixin, CreateView):
    model = StudentInfo
    template_name = 'join.html'
    success_url = '/'
    form_class = StudentForm

    def dispatch(self, request, *args, **kwargs):
        #최초 로그인이 아니거나 로그인 상태가 아니면 메인 화면으로 리다이렉트
        studentInfo = StudentInfo.get_student(self.request.user.id)
        if studentInfo is not None:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class MypageLV(DefaultMixin, LoginRequiredMixin, ListView):
    model = University
    template_name = 'mypage.html'
    active = 'mypageActive'