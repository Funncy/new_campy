from rest_framework import serializers

from .models import Subject, Lecture
from university.serializers import CompletiondivisionSerializer, AreaSerializer

class SubjectSerializer(serializers.ModelSerializer):
    completion_division = CompletiondivisionSerializer(read_only=True)
    area = AreaSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = ('__all__')

class LectureSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer
    class Meta:
        model = Lecture
        fields = ('__all__')