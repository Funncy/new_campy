from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from student.models import StudentInfo, StudentAddedMajor
from .mixin import DefaultMixin, LoginRequiredMixin, ActiveMixin, StudentInfoMixin
from university.mixin import UniversityMixin
from .forms import StudentForm
from .models import StudentAddedMajor, StudentInfo
# Create your views here.

class JoinCV(StudentInfoMixin, ActiveMixin, LoginRequiredMixin, UniversityMixin, CreateView):
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

        # 학과 중복 검사 및 저장
        StudentAddedMajor.save_or_update_added_majors(form, user.id)

        if form.errors:
            return super().form_invalid(form)

        form.save()
        return super().form_valid(form)


class MypageUV(DefaultMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StudentInfo
    template_name = 'mypage.html'
    form_class = StudentForm
    active = 'mypageActive'
    success_message = '수정완료하였습니다.'

    # 다른 유저의 Mypage 접근 차단
    def dispatch(self, request, *args, **kwargs):
        student_info = StudentInfo.objects.values('id').get(user_id=request.user.id)
        if self.kwargs['pk'] != student_info['id']:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_initial(self):
        return StudentAddedMajor.get_added_major_context(self.request.user.id)

    def form_valid(self, form):
        # 유저 연결
        user = self.request.user
        form.instance.user = user

        #학과 중복 검사 및 저장
        StudentAddedMajor.save_or_update_added_majors(form, user.id)

        if form.errors:
            return super().form_invalid(form)

        form.save()
        return super().form_valid(form)

