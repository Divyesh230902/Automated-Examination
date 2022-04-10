import imp
from django.db import models
from Examination.models import StudentAnswersheet

# Create your models here.
class MarksObtained(models.Model):
    answersheet = models.ForeignKey(StudentAnswersheet,on_delete=models.CASCADE)
    marks = models.SmallIntegerField()
    checked_at = models.DateTimeField(auto_now_add = True)
    sent = models.BooleanField(default=False)
    