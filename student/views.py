from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from university.models import University
from student.models import StudentInfo
from campy.views import StudentInfoMixin

# Create your views here.

class JoinLV(StudentInfoMixin, ListView):
    model = University
    template_name = 'join.html'

    def dispatch(self, request, *args, **kwargs):
        studentInfo = StudentInfo.get_student(self.request.user.id)
        if studentInfo is not None or self.request.user.id is None:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

class MypageLV(StudentInfoMixin, ListView):
    model = University
    template_name = 'mypage.html'
