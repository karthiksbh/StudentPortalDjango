from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.

CLASSES = (
    ('Class 8', 'Class 8'),
    ('Class 9', 'Class 9'),
    ('Class 10', 'Class 10'),
    ('Class 11', 'Class 11'),
    ('Class 12', 'Class 12'),
)


class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    class_student = models.CharField(
        max_length=100, choices=CLASSES)
    student_email = models.EmailField(max_length=200)
    mobile_number = models.IntegerField()
    school = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class todo_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
