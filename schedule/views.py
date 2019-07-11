from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from student.mixin import DefaultMixin, LoginRequiredMixin
from .models import Schedule
# Create your views here.

class ScheduleLV(DefaultMixin, LoginRequiredMixin, ListView):
    model = Schedule
    #현재 html파일 없음
    template_name = 'schedule_list.html'
    active = 'scheduleActive'

class ScheduleCV(DefaultMixin, LoginRequiredMixin, CreateView):
    model = Schedule
    template_name = 'schedule_form.html'
    fields = ('name', 'lectures')
    active = 'scheduleActive'
    success_url = '/schedule/'

class ScheduleUV(DefaultMixin, LoginRequiredMixin, UpdateView):
    model = Schedule
    template_name = 'schedule_form.html'
    fields = ('name', 'lectures')
    active = 'scheduleActive'
    success_url = '/schedule/'