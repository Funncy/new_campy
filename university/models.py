from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(verbose_name='대학이름', max_length=30)
    # minimum_credit = models.FloatField(verbose_name='최소학점')
    maximum_credit = models.FloatField(verbose_name='최대학점')

class CompletionDivision(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='영역이름', max_length=10)
    group_name = models.CharField(verbose_name='그룹이름', max_length=10)

class Area(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='영역이름', max_length=10)

class Community(models.Model):
    name = models.CharField(verbose_name='커뮤니티이름', max_length=20)

class Track(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='트랙이름', max_length=20)

class Department(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='학과이름', max_length=20)
    college_name = models.CharField(verbose_name='단과대학이름', max_length=20)
    same_department = models.ForeignKey('self', verbose_name='동일학과', on_delete=models.CASCADE, blank=True, null=True)
    community = models.ForeignKey(Community, verbose_name='커뮤니티그룹', on_delete=models.CASCADE, blank=True, null=True)
