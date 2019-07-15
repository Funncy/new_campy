from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from student.mixin import DefaultMixin, StaffRequiredMixin
from .models import Lecture, Subject
from .serializers import SubjectSerializer, LectureSerializer

# Create your views here.

'''
 UI CLASS
'''
class SubjectLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Subject
    template_name = 'subject_list.html'
    active = 'subjectManagementActive'

class LectureLV(DefaultMixin, StaffRequiredMixin, ListView):
    model = Lecture
    template_name = 'lecture_list.html'
    active = 'lectureManagementActive'

'''
 FILE UPLOAD 로직
'''
@login_required
def LectureUploadFV(request):
    if request.user.is_staff is False:
        return redirect(reverse('index'))
    context = {}
    context['dataUploadActive'] = True
    #GET, POST로 엑셀 파일 로직 추가
    return render(request, 'lecture_upload.html', context)


'''
 API 
'''
class SubjectReadViewset(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )