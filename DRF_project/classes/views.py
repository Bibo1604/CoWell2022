from lib2to3.pytree import Base
from django.shortcuts import render
from .models import Class
from .serializers import ClassSerializer
from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class PostUserWritePermission(BasePermission):
    message = "Editing class detail is restricted to teacher only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.teacher ==request.user

# class ClassList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer

# class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserWritePermission]
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer

class ClassView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, PostUserWritePermission]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
