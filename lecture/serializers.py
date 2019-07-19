from rest_framework import serializers

from .models import Subject, Lecture, LectureTime
from university.serializers import CompletiondivisionSerializer, AreaSerializer

class SubjectSerializer(serializers.ModelSerializer):
    completion_division = CompletiondivisionSerializer(read_only=True)
    area = AreaSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = ('__all__')

class LectureTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureTime
        fields = ('week', 'start_time', 'end_time')

class LectureSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    times = LectureTimeSerializer(many=True, read_only=True)
    class Meta:
        model = Lecture
        fields = ('subject', 'professor', 'class_room', 'class_year', 'opened_year',
                  'opened_semester', 'opened_college', 'opened_department', 'times')