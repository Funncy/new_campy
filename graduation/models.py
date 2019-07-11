from django.db import models
from university.models import CompletionDivision, Track

# Create your models here.
class SubjectGroup(models.Model):
    completion_divisions = models.ManyToManyField(CompletionDivision, verbose_name='이수구분들')
    name = models.CharField(verbose_name='그룹명', max_length=20)

class RuleGeneral(models.Model):
    name = models.CharField(verbose_name='졸업요건명', max_length=20)
    track = models.ForeignKey(Track, verbose_name='트랙', on_delete=models.CASCADE)
    type = models.CharField(verbose_name='졸업요건타입', max_length=20)
    value = models.SmallIntegerField(verbose_name='졸업요건값', default=0)
    subject_group = models.ForeignKey(SubjectGroup, verbose_name='과목그룹', on_delete=models.CASCADE)

class RuleSpecific(models.Model):
    name = models.CharField(verbose_name='졸업요건명', max_length=20)
    track = models.ForeignKey(Track, verbose_name='트랙', on_delete=models.CASCADE)
    type = models.CharField(verbose_name='졸업요건타입', max_length=20)
    value = models.SmallIntegerField(verbose_name='졸업요건값', default=0)
    upper_rule = models.ForeignKey(RuleGeneral, verbose_name='상위졸업요건', on_delete=models.CASCADE, null=True, blank=True)
    subject_group = models.ForeignKey(SubjectGroup, verbose_name='과목그룹', on_delete=models.CASCADE)