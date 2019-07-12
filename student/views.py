from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from university.models import University
from student.models import StudentInfo, StudentAddedMajor
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

    def form_valid(self, form):

        # 유저 연결
        user = self.request.user
        form.instance.user = user

        #부/복수 전공 저장
        multi_major = None
        sub_major = None
        if form.cleaned_data['multi_major'] is not None:
            multi_major = form.cleaned_data['multi_major'].id
        if form.cleaned_data['sub_major'] is not None:
            sub_major = form.cleaned_data['sub_major'].id

        #주전공 - 복수전공/부전공 중복
        if form.instance.major_id == multi_major or form.instance.major_id == sub_major:
            form.add_error("major", "학과를 중복 선택하였습니다.")
            return self.form_invalid(form)

        #부전공 - 복수전공 중복
        if multi_major is not None and multi_major == sub_major:
            form.add_error("major", "학과를 중복 선택하였습니다.")
            return self.form_invalid(form)

        if multi_major is not None:
            StudentAddedMajor.save_added_major(multi_major, user.id, 'multi_major')
        if sub_major is not None:
            StudentAddedMajor.save_added_major(sub_major, user.id, 'sub_major')

        form.save()
        return super().form_valid(form)


class MypageLV(DefaultMixin, LoginRequiredMixin, ListView):
    model = University
    template_name = 'mypage.html'
    active = 'mypageActive'