from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from Examination.models import StudentAnswersheet
from Evaluation.serializers import MarksObtainedSerializer
from .utils import sort_answersheets
from Examination.models import Exam

# Create your views here.

class MarksObtainedAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MarksObtainedSerializer

class SendResultAPIView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self,request):
        exam = request.data.get('exam')
        sem = request.data.get('semester')
        year = request.data.get("year")
        if exam and sem and year:
            answersheets = StudentAnswersheet.objects.filter(exam__type = exam,
             exam__semester = sem, exam__date__year = year)
            sort_answersheets(answersheets,Exam.Type(exam).label,year)
            if answersheets:
                return Response({
                    "message":"Result has sent"
                })
            else:
                return Response({
                    "message":"No Result Found"
                },status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                    "message":"Data not provided"
                })
