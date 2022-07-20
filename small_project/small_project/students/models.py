from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    grade = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.user', related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
