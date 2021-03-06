from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from lecture.models import Lecture
from student.mixin import DefaultMixin, LoginRequiredMixin
from student.models import StudentInfo
from university.models import CompletionDivision
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        #학생데이터로 대학 정보 가져오기
        student = StudentInfo.objects.get(user_id=self.request.user.id)
        university_id = student.university_id
        context['student_department'] = student.major.name

        # 강의에서 학과 데이터
        departments = Lecture.objects.values('opened_department').order_by('opened_department').distinct()
        context['department_list'] = departments

        # 강의에서 이수구분 데이터
        divisions = CompletionDivision.objects.filter(university_id=university_id)
        context['division_list'] = divisions

        #강의 학년 학기 필터링
        # 임시 2013년 1학기(10)

        lectures = Lecture.objects.filter(
            opened_year=2013,
            opened_semester=10,
            subject__university_id=university_id
        )

        #페이지네이션
        page = self.request.GET.get('page', 1)

        paginator = Paginator(lectures, 15)
        try:
            lecture_list = paginator.page(page)
        except PageNotAnInteger:
            lecture_list = paginator.page(1)
        except EmptyPage:
            lecture_list = paginator.page(paginator.num_pages)

        current_page = int(page) if page else 1
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        context['lecture_list'] = lecture_list
        return context

class ScheduleUV(DefaultMixin, LoginRequiredMixin, UpdateView):
    model = Schedule
    template_name = 'schedule_form.html'
    fields = ('name', 'lectures')
    active = 'scheduleActive'
    success_url = '/schedule/'