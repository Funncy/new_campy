from rest_framework import serializers

from .models import Department, CompletionDivision, Area, Track, University

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('__all__')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('__all__')

class CompletiondivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionDivision
        fields = ('__all__')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('__all__')