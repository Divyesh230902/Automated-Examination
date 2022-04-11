from rest_framework import serializers

from Dtail.models import Student
from .models import AnswerSheet, StudentAnswersheet

class StudentAnswerSheetSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(slug_field='qr_code',queryset=Student.objects.all())
    answersheet = serializers.SlugRelatedField(slug_field='qr_code',queryset=AnswerSheet.objects.all())
    class Meta:
        model = StudentAnswersheet
        fields = "__all__"
    
    