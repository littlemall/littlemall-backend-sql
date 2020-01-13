
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Feuser
from .serializers import FeuserSerializer


# 使用APIView
class FeuserView(APIView):
  def get(self, request, format=None):
    feuser = Feuser.objects.all()
    serializer = FeuserSerializer(feuser, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = FeuserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)