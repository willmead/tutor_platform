from django.contrib import admin
from .models import Subject, Student, Profile, Lesson, Invoice, Group


# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(Invoice)
admin.site.register(Group)
