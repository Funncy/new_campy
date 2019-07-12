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
    user = models.OneToOneField(User, verbose_name='유저', on_delete=models.CASCADE)
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    major = models.ForeignKey(Department, verbose_name='주전공', on_delete=models.CASCADE)
    admission_year = models.SmallIntegerField(verbose_name='입학년도')

    def get_student(pk):
        try:
            return StudentInfo.objects.get(user_id=pk)
        except StudentInfo.DoesNotExist:
            return None

class StudentAddedMajor(models.Model):
    user = models.ForeignKey(StudentInfo, verbose_name='유저정보', on_delete=models.CASCADE)
    major_division = models.CharField(verbose_name='전공구분', max_length=20)
    major = models.ForeignKey(Department, verbose_name='전공학과', on_delete=models.CASCADE)

    def save_added_major(major, user_id, major_division=''):
        major = StudentAddedMajor(
            user_id=user_id,
            major_id=major,
            major_division=major_division
        )
        major.save()
