from numpy import source
from rest_framework import serializers

from Examination.models import StudentAnswersheet
from .models import MarksObtained

class MarksObtainedSerializer(serializers.ModelSerializer):
    answersheet = serializers.UUIDField(source="answersheet.qr_code")

    class Meta:
        model = MarksObtained
        fields = "__all__"
    
