from django.contrib import admin
from .models import Subject, Student, Profile, Lesson


# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Lesson)
