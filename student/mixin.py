from .models import StudentInfo


class StudentInfoMixin(object):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentInfo.get_student(self.request.user.id)
        return context