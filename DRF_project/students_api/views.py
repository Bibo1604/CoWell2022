from django.shortcuts import render
from students.models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'Classes': reverse('classes:classes-list', request=request, format=format),
        'Teachers': reverse('teachers:teachers-list', request=request, format=format),
        'Students': reverse('students:students-list', request=request, format=format),
    })

class PostUserWritePermission(BasePermission):
    message = 'Editing students detail is restricted to the teacher only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.teacher == request.user

# class StudentList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, PostUserWritePermission]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer