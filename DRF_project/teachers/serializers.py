from dataclasses import field
from rest_framework import serializers
from teachers.models import NewTeacher

class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewTeacher
        fields = ('email', 'username', 'name', 'password', 'url')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance