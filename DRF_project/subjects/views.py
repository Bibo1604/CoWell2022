from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class SubjectView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
