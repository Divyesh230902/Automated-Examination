from rest_framework import serializers
from .models import StudentAnswersheet

class StudentAnswerSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswersheet
        fields = "__all__"