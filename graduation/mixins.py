

from university.models import Track


'''
header.html 에 뿌려줄 학생 정보 데이터 가져오는 믹스인
'''

class RuleDefaultDataMixin(object):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traks'] = Track.objects.filter(university=self.kwargs['university'])
        YEAR = [x for x in reversed(range(1950, 2021))]
        context['years'] = YEAR
        return context