from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentAnswersheetAPIview(generics.GenericAPIView):
    pass 

class CheckInvigilator(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]