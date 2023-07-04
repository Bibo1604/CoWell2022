from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from teachers.models import NewTeacher
from rest_framework import viewsets

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        register_serializer = RegisterUserSerializer(data = request.data)
        if register_serializer.is_valid():
            new_user = register_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TeacherList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = NewTeacher.objects.all()
#     serializer_class = RegisterUserSerializer

# class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = NewTeacher.objects.all()
#     serializer_class = RegisterUserSerializer

class TeacherView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NewTeacher.objects.all()
    serializer_class = RegisterUserSerializer