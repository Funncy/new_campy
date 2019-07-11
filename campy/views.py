from django.shortcuts import render
from django.views.generic import TemplateView
from student.mixin import StudentInfoMixin

class IndexTV(StudentInfoMixin, TemplateView):
    template_name = 'index.html'

def test(request):
    return render(request, 'test.html', {})