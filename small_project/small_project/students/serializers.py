from rest_framework import serializers
from students.models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(many=True, view_name='student-detail', read_only=True)
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'students', 'owner']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Student
        fields = ['url', 'owner', 'id', 'name', 'birthday', 'grade', 'comment']