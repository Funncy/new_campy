from django.db import models
from university.models import Area, CompletionDivision, University, Department
# Create your models here.

class Subject(models.Model):
    code = models.CharField(verbose_name='교과목코드', max_length=20, primary_key=True)
    name = models.CharField(verbose_name='교과목명', max_length=20)
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    completion_division = models.ForeignKey(CompletionDivision, verbose_name='이수구분', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, verbose_name='영역', on_delete=models.CASCADE)
    credit = models.FloatField(default=0)

class Lecture(models.Model):
    code = models.CharField(verbose_name='강의코드', max_length=20)
    subject = models.ForeignKey(Subject, verbose_name='교과목', on_delete=models.CASCADE)
    professor = models.CharField(verbose_name='교수님', max_length=10)
    class_room = models.CharField(verbose_name='강의실', max_length=15)
    week = models.CharField(verbose_name='요일', max_length=5)
    start_time = models.TimeField(verbose_name='시작시간')
    end_time = models.TimeField(verbose_name='끝나는시간')
    opened_year = models.SmallIntegerField(verbose_name='개설년도')
    opened_semester = models.SmallIntegerField(verbose_name='개설학기')
    opened_department = models.ForeignKey(Department, verbose_name='개설학과', on_delete=models.CASCADE)
