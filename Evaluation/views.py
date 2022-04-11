from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Evaluation.serializers import MarksObtainedSerializer

# Create your views here.

class MarksObtainedAPIView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = MarksObtainedSerializer
