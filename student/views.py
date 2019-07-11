from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from university.models import University
from student.models import StudentInfo
from .mixin import ActiveMixin, StudentInfoMixin, LoginRequiredMixin

# Create your views here.

class JoinLV(ActiveMixin, LoginRequiredMixin, StudentInfoMixin, ListView):
    model = University
    template_name = 'join.html'

    def dispatch(self, request, *args, **kwargs):
        #최초 로그인이 아니거나 로그인 상태가 아니면 메인 화면으로 리다이렉트
        studentInfo = StudentInfo.get_student(self.request.user.id)
        if studentInfo is not None:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class MypageLV(ActiveMixin, LoginRequiredMixin, StudentInfoMixin, ListView):
    model = University
    template_name = 'mypage.html'
    active = 'mypageActive'