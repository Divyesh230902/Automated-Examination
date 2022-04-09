from django.db import models
from Dtail.models import Branch

# Create your models here.

class Subject(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True,max_length=50)

class Exam(models.Model):
    class Semester(models.IntegerChoices):
        FIRST = 1, '1'
        SECOND = 2, '2'
        THIRD = 3, '3'
        FORTH = 4, '4'
        FIFTH = 5, '5'
        SIXTH = 6, '6'
        SEVENTH = 7, '7'
        EIGHTH = 8, '8'

    class Type(models.TextChoices):
        MID_SEM = 'MS', 'MID SEMESTER'
        END_SEM = 'ES', 'END SEMESTER'
        INTERMEDIATE = 'IM', 'INTERMEDIATE'
    type = models.CharField(max_length=2,choices=Type.choices)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    date = models.DateField()
    marks = models.IntegerField()
    semester = models.IntegerField(choices=Semester.choices)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='exam_branch')