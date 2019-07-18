from django.db import models
from student.models import StudentInfo
from university.models import Area, CompletionDivision, University, Department
# Create your models here.

class Subject(models.Model):
    code = models.CharField(verbose_name='교과목코드', max_length=20, primary_key=True)
    name = models.CharField(verbose_name='교과목명', max_length=20)
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    completion_division = models.ForeignKey(CompletionDivision, verbose_name='이수구분', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, verbose_name='영역', on_delete=models.CASCADE)
    credit = models.FloatField(default=0)

    def get_university_subject_list(user_id):
        student_info = StudentInfo.objects.get(user_id=user_id)
        return Subject.objects.filter(university=student_info.university)

class Lecture(models.Model):
    SEMESTER_CHOICES = (
        (10, '1학기'),
        (20, '2학기'),
        (11, '여름학기'),
        (21, '겨울학기'),
    )
    subject = models.ForeignKey(Subject, verbose_name='교과목', on_delete=models.CASCADE)
    professor = models.CharField(verbose_name='교수님', max_length=10)
    class_room = models.CharField(verbose_name='강의실', max_length=15)
    opened_year = models.SmallIntegerField(verbose_name='개설년도')
    opened_semester = models.SmallIntegerField(verbose_name='개설학기', choices=SEMESTER_CHOICES, default=0)
    opened_college = models.CharField(verbose_name='개설단', max_length=50)
    opened_department = models.CharField(verbose_name='개설학과', max_length=50)

class LectureTime(models.Model):
    WEEK_CHOICES = (
        ('mon', '월'),
        ('tue', '화'),
        ('wed', '수'),
        ('thu', '목'),
        ('fir', '금'),
        ('sat', '토'),
    )
    lecture = models.ForeignKey(Lecture, verbose_name='강의', on_delete=models.CASCADE)
    week = models.CharField(verbose_name='요일', choices=WEEK_CHOICES, max_length=10)
    start_time = models.TimeField(verbose_name='시작시간')
    end_time = models.TimeField(verbose_name='끝나는시간')