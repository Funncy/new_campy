from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

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

    def get_student(pk):
        try:
            return StudentInfo.objects.get(user_id=pk)
        except StudentInfo.DoesNotExist:
            return None

    def get_absolute_url(self):
        return reverse('mypage', args=[self.id])

class StudentAddedMajor(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    major_division = models.CharField(verbose_name='전공구분', max_length=20)
    major = models.ForeignKey(Department, verbose_name='전공학과', on_delete=models.CASCADE)

    def save_added_major(major, user_id, major_division=''):
        major = StudentAddedMajor(
            user_id=user_id,
            major_id=major,
            major_division=major_division
        )
        major.save()

    def save_or_update_added_majors(form, user_id):
        # 부/복수 전공 저장
        multi_major = None
        sub_major = None
        if form.cleaned_data['multi_major'] is not None:
            multi_major = form.cleaned_data['multi_major'].id
        if form.cleaned_data['sub_major'] is not None:
            sub_major = form.cleaned_data['sub_major'].id

        # 주전공 - 복수전공/부전공 중복
        if form.instance.major_id == multi_major or form.instance.major_id == sub_major:
            form.add_error("major", "학과를 중복 선택하였습니다.")
            return form

        # 부전공 - 복수전공 중복
        if multi_major is not None and multi_major == sub_major:
            form.add_error("major", "학과를 중복 선택하였습니다.")
            return form

        # 이미 저장된 복수/부 전공등 삭제 (업데이트용)
        StudentAddedMajor.objects.filter(user_id=user_id).delete()

        if multi_major is not None:
            StudentAddedMajor.save_added_major(multi_major, user_id, 'multi_major')
        if sub_major is not None:
            StudentAddedMajor.save_added_major(sub_major, user_id, 'sub_major')
        return form

    def get_added_major_context(user_id):
        majors = StudentAddedMajor.objects.filter(user_id=user_id)
        context = {}
        for major in majors:
            context[major.major_division] = major.major_id
        return context
