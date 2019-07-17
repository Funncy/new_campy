from django.db import models

# Create your models here.

class University(models.Model):
    FIRST = 4.5
    SECOND = 4.3
    THIRD = 4.0
    CREDIT_CHOICES = (
        (FIRST, '4.5'),
        (SECOND, '4.3'),
        (THIRD, '4.0'),
    )

    name = models.CharField(verbose_name='대학이름', max_length=30)
    # minimum_credit = models.FloatField(verbose_name='최소학점')
    maximum_credit = models.FloatField(verbose_name='최대학점', default=4.5, choices=CREDIT_CHOICES)

class CompletionDivision(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='영역이름', max_length=10)
    group_name = models.CharField(verbose_name='그룹이름', max_length=10, blank=True)

    def get_division_by_university(university_id):
        return CompletionDivision.objects.filter(university=university_id)

class Area(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='영역이름', max_length=10)

    def get_area_by_university(university_id):
        return Area.objects.filter(university=university_id)

class Community(models.Model):
    name = models.CharField(verbose_name='커뮤니티이름', max_length=20)

class Track(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='트랙이름', max_length=20)

    def get_track_by_university(university_id):
        return Track.objects.filter(university=university_id)

class Department(models.Model):
    university = models.ForeignKey(University, verbose_name='대학', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='학과이름', max_length=20)
    college_name = models.CharField(verbose_name='단과대학이름', max_length=20)
    same_department = models.ForeignKey('self', verbose_name='동일학과', on_delete=models.CASCADE, blank=True, null=True)
    community = models.ForeignKey(Community, verbose_name='커뮤니티그룹', on_delete=models.CASCADE, blank=True, null=True)

