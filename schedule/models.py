from django.db import models
from django.contrib.auth.models import User
from lecture.models import Lecture

# Create your models here.
class Schedule(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='시간표이름', max_length=20)
    lectures = models.ManyToManyField(Lecture, verbose_name='강의들')
