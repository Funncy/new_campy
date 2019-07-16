

from .models import University


'''
대학 정보를 뿌려주는 믹스인
'''
class UniversityMixin(object):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['university_list'] = University.objects.all()
        return context