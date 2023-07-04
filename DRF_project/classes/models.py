from django.db import models
from students.models import Student
from teachers.models import NewTeacher

class Class(models.Model):
    class_name = models.CharField(max_length=100, blank=False)
    students_list = models.ManyToManyField(Student, blank=True)
    teacher = models.ForeignKey(NewTeacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name
