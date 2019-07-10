from django.db import models
from django.contrib.auth.models import User
from university.models import University, Department

# Create your models here.

'''
학생 정보
join 에서 최초 입력
mypage 에서 수정
'''
class StudentInfo(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    major = models.ForeignKey(Department, verbose_name='주전공', on_delete=models.CASCADE)
    admission_year = models.SmallIntegerField(verbose_name='입학년도')

class StudentAddedMajor(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    major_division = models.CharField(verbose_name='전공구분', max_length=10)
    major = models.ForeignKey(Department, verbose_name='전공학과', on_delete=models.CASCADE)
