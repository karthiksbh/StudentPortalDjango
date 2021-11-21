from django.contrib import admin
from .models import (StudentProfile, todo_list)


# Register your models here.


@admin.register(StudentProfile)
class StudentProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'student_name',
                    'class_student', 'student_email', 'mobile_number', 'school', 'city']


@admin.register(todo_list)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'desc', 'done']
