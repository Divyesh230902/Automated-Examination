from rest_framework import serializers

class StudentAnswerSheetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"