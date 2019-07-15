from django.db import models
from django.contrib.auth.models import User

from student.models import StudentInfo
from university.models import University, CompletionDivision
from lecture.models import Subject

# Create your models here.
'''
이수학기 1 = 1학기 2 = 2학기 3 = 여름학기 4 = 겨울학기
'''
class LectureHistory(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='과목', on_delete=models.CASCADE)
    grade = models.CharField(verbose_name='학생성적', max_length=10, default='F')
    completion_year = models.SmallIntegerField(verbose_name='이수학년')
    completion_semester = models.SmallIntegerField(verbose_name='이수학기')
    completion_division = models.ForeignKey(CompletionDivision, verbose_name='이수구분', on_delete=models.CASCADE)

    def get_user_history(user_id):
        student_info = StudentInfo.objects.get(user_id=user_id)
        return LectureHistory.objects.filter(user_id=user_id, university=student_info.university)