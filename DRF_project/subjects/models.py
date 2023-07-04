from django.db import models
from classes.models import Class
from teachers.models import NewTeacher

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=False)
    class_list = models.ManyToManyField(Class, blank= True)
    teacher_list = models.ManyToManyField(NewTeacher, blank=True)

    def __str__(self):
        return self.subject_name

