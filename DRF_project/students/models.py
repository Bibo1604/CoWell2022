from django.db import models
from django.conf import settings

class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    grade = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

