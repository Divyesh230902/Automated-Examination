from django.contrib import admin
from .models import AnswerSheet, Invigilagtor, StudentAnswersheet, Subject, Exam

# Register your models here.
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(AnswerSheet)
admin.site.register(StudentAnswersheet)
admin.site.register(Invigilagtor)