from rest_framework import serializers

from .models import LectureHistory

class LectureHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureHistory
        fields = ('__all__')