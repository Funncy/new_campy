from rest_framework import serializers

from .models import LectureHistory
from lecture.serializers import SubjectSerializer
from university.serializers import CompletiondivisionSerializer

class LectureHistorySerachSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    completion_division = CompletiondivisionSerializer(read_only=True)
    class Meta:
        model = LectureHistory
        fields = ('__all__')

class LectureHistoryChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureHistory
        fields = ('__all__')
        read_only_fields = ('user', )