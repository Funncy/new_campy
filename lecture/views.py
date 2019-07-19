from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, FormView
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from student.mixin import DefaultMixin, StaffRequiredMixin
from student.models import StudentInfo
from university.models import University, CompletionDivision, Area
from .models import Lecture, Subject
from .serializers import SubjectSerializer, LectureSerializer
from .forms import UploadFileForm

from .excel.excel_to_data import LectureExcel

# Create your views here.

'''
 UI CLASS
'''
class SubjectLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Subject
    template_name = 'subject_list.html'
    active = 'subjectManagementActive'
    paginate_by = 15

    def get_queryset(self):
        search_name = self.request.GET.get('search_name', '')
        return Subject.search_subject(search_name, self.kwargs['division'],
                                      self.kwargs['area'], self.kwargs['university'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #페이지 네이션 수
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        #Search 데이터 넣어주기
        context['current_university'] = self.kwargs['university']
        context['current_division'] = self.kwargs['division']
        context['current_area'] = self.kwargs['area']

        #Search Bar 용 대학, 이수구분, 영역 넣어주기
        context['university_list'] = University.objects.all()
        context['division_list'] = CompletionDivision.objects.filter(university_id=self.kwargs['university'])
        context['area_list'] = Area.objects.filter(university_id=self.kwargs['university'])

        #Search 내용 넣어주기
        context['search_name'] = self.request.GET.get('search_name', '')
        return context

class LectureLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Lecture
    template_name = 'lecture_list.html'
    active = 'lectureManagementActive'
    paginate_by = 15

    def get_queryset(self):
        search_name = self.request.GET.get('search_name', '')
        if search_name:
            return Lecture.objects.filter(subject__university_id=self.kwargs['university'],
                                          subject__name__contains=search_name)
        return Lecture.objects.filter(subject__university_id=self.kwargs['university'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #페이지 네이션 수
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        #Search 데이터 넣어주기
        context['current_university'] = self.kwargs['university']

        #Search Bar 용 대학, 이수구분, 영역 넣어주기
        context['university_list'] = University.objects.all()
        #Search 내용 넣어주기
        context['search_name'] = self.request.GET.get('search_name', '')
        return context

'''
 FILE UPLOAD 로직
'''
class LectureUploadFV(DefaultMixin, StaffRequiredMixin, FormView):
    form_class = UploadFileForm
    template_name = 'lecture_upload.html'
    active = 'dataUploadActive'

    def form_valid(self, form):
        filehandle = form.files['file']
        university_id = form.cleaned_data['university'].id
        lecture_excel = LectureExcel()
        lecture_excel.excel_process(filehandle, university_id)
        return redirect(reverse('lecture_list', kwargs={'university':university_id}))


'''
 API 
'''

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SubjectReadViewset(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )

class LectureReadViewset(ReadOnlyModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        #학생정보러 대학 필터링
        university_id = StudentInfo.get_university_id(self.request.user.id)

        #학과, 이수구분으로 데이터 필터링
        division = self.request.query_params.get('division')
        department = self.request.query_params.get('department')

        #추가 필터링

        return Lecture.get_lectures(university_id, division, department)


