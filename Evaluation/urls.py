from django.urls import path

from Evaluation.views import MarksObtainedAPIView

urlpatterns = [
    path("add-marks/",MarksObtainedAPIView.as_view()),
]