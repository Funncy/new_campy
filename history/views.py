from django.shortcuts import render
from django.views.generic import ListView
from .models import LectureHistory
from student.mixin import ActiveMixin, LoginRequiredMixin

# Create your views here.

class LectureHistoryLV(ActiveMixin, LoginRequiredMixin, ListView):
    model = LectureHistory
    template_name = 'lecture_history.html'
    active = 'lectureHistoryActive'

    def get_queryset(self):
        return LectureHistory.objects.filter(user_id=self.request.user.id)
