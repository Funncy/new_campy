from django.db import models
from university.models import CompletionDivision, Track, University, Department

# Create your models here.
class SubjectGroup(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='그룹명', max_length=20)
    completion_divisions = models.ManyToManyField(CompletionDivision, verbose_name='이수구분들')

class RuleGeneral(models.Model):
    RULE_TYPE_CHOICES = (
        (1, '학점총합'),
        (2, '과목갯수'),
        (3, '영역갯수'),
        (4, '학점평균'),
    )
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='졸업요건명', max_length=20)
    track = models.ForeignKey(Track, verbose_name='트랙', on_delete=models.CASCADE)
    year = models.SmallIntegerField(default=0)
    type = models.SmallIntegerField(verbose_name='졸업요건타입', choices=RULE_TYPE_CHOICES, default=1)
    value = models.SmallIntegerField(verbose_name='졸업요건값', default=0)
    subject_group = models.ForeignKey(SubjectGroup, verbose_name='과목그룹', on_delete=models.CASCADE)

class RuleSpecific(models.Model):
    RULE_TYPE_CHOICES = (
        (1, '학점총합'),
        (2, '과목갯수'),
        (3, '영역갯수'),
        (4, '학점평균'),
    )
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='학과', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='졸업요건명', max_length=20)
    track = models.ForeignKey(Track, verbose_name='트랙', on_delete=models.CASCADE)
    year = models.SmallIntegerField(default=0)
    type = models.SmallIntegerField(verbose_name='졸업요건타입', choices=RULE_TYPE_CHOICES, default=1)
    value = models.SmallIntegerField(verbose_name='졸업요건값', default=0)
    upper_rule = models.ForeignKey(RuleGeneral, verbose_name='상위졸업요건', on_delete=models.CASCADE, null=True, blank=True)
    change_rule = models.ForeignKey('self', verbose_name='특정룰 변경', on_delete=models.CASCADE, null=True, blank=True)
    subject_group = models.ForeignKey(SubjectGroup, verbose_name='과목그룹', on_delete=models.CASCADE)
