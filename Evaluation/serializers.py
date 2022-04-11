from rest_framework import serializers

from Examination.models import StudentAnswersheet,AnswerSheet
from .models import MarksObtained


class MarksObtainedSerializer(serializers.ModelSerializer):
    answersheet = serializers.UUIDField(source="answersheet.answersheet.qr_code")

    class Meta:
        model = MarksObtained
        fields = "__all__"

    def create(self, validated_data):
        ans_sheet = validated_data['answersheet']['answersheet']["qr_code"]
        ans_sheet = AnswerSheet.objects.get(qr_code = ans_sheet)
        obj = MarksObtained.objects.create(
            answersheet=StudentAnswersheet.objects.get(
                answersheet=ans_sheet),
            marks=validated_data['marks'],
            examiner=validated_data["examiner"]
        )
        obj.save()
        return obj