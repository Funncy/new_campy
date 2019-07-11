from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, reverse

from .models import StudentInfo


'''
header.html 에 뿌려줄 학생 정보 데이터 가져오는 믹스인
'''
class StudentInfoMixin(object):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentInfo.get_student(self.request.user.id)
        return context

'''
header.html 에 선택 메뉴 활성화를 위환 믹스인
'''
class ActiveMixin(object):
    active = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.active] = True
        return context

class DefaultMixin(StudentInfoMixin, ActiveMixin):
    pass

'''
로그인한 상태인지 확인하는 믹스인
'''
class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

'''
관리자인지 확인하는 믹스인
'''
class StaffRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        #관리자가 아닌경우 메인으로 리다이렉트
        if self.request.user.is_staff is False:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)