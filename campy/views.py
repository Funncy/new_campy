from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from student.models import StudentInfo


## 실 사용 list
def Index(request):
    context = {
        'student': StudentInfo.get_student(request.user.id)
    }
    return render(request, 'index.html', context)

def test(request):
    return render(request, 'test.html', {})