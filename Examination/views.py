from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from Examination.serializers import StudentAnswerSheetSerializer
from .models import Invigilagtor

# Create your views here.
class StudentAnswersheetAPIview(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentAnswerSheetSerializer


class CheckInvigilator(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        today = datetime.now().date()
        data = Invigilagtor.objects.filter(professor__user = request.user,exam__date = today)
        if data.exists():
            return Response(
                {
                    "exam_id":data[0].exam.id
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                "message":"No Exam Found"
            },status=status.HTTP_404_NOT_FOUND)
