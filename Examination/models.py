import uuid
from django.db import models
from Dtail.models import Branch, Professor, Student

# Create your models here.

class Subject(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True,max_length=50)

    def __str__(self) -> str:
        return self.name

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

    def __str__(self) -> str:
        return f'{self.type}  Semester:{self.semester}  Branch:{self.branch.name} ' \
            f'Year:{self.date.year} Subject:{self.subject.name}'

class AnswerSheet(models.Model):
    qr_code = models.UUIDField(unique=True,default=uuid.uuid4)
    
    def __str__(self) -> str:
        return str(self.id)
    
class StudentAnswersheet(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    answersheet = models.OneToOneField(AnswerSheet, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    invigilator = models.ForeignKey(Professor,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.student.__str__()}   AnsSheet:{self.answersheet.__str__()}'

class Invigilagtor(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.exam.__str__()}   Professor:{self.professor.__str__()}'
