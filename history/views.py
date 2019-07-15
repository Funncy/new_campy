from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import LectureHistory
from .serializers import LectureHistorySerializer
from student.mixin import DefaultMixin, LoginRequiredMixin
from lecture.models import Subject

# Create your views here.

'''
 UI CLASS
'''
class LectureHistoryLV(DefaultMixin, LoginRequiredMixin, ListView):
    model = LectureHistory
    template_name = 'lecture_history.html'
    active = 'lectureHistoryActive'

    def get_queryset(self):
        return LectureHistory.objects.filter(user_id=self.request.user.id)

    # 과목 데이터 로드
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.get_university_subject_list(self.request.user.id)
        return context

'''
 API ViewSet
'''

class LectureHistoryListViewset(ModelViewSet):
    queryset = LectureHistory.objects.all()
    serializer_class = LectureHistorySerializer
    permission_classes = (IsAuthenticated)

    def get_queryset(self):
        return LectureHistory.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)