from rest_framework import serializers
from classes.models import Class

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'class_name', 'students_list', 'teacher', 'url')