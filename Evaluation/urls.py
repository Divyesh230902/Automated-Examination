from django.urls import path

from Evaluation.views import MarksObtainedAPIView, SendResultAPIView

urlpatterns = [
    path("add-marks/",MarksObtainedAPIView.as_view()),
    path("send-result/",SendResultAPIView.as_view()),
]