from django.urls import path

from Examination.views import CheckInvigilator, StudentAnswersheetAPIview

urlpatterns = [
    path("get-exam/",CheckInvigilator.as_view()),
    path("add-student-answersheet/",StudentAnswersheetAPIview.as_view()),
]