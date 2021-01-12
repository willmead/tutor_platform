from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    notes = models.TextField()
    rate_per_hour = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.user.username



class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration_in_hours = models.FloatField()
    topic = models.CharField(max_length=256, default="General")
    report = models.TextField()
    is_invoiced = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} ({self.date})"


class Invoice(models.Model):
    lessons = models.ManyToManyField(Lesson)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
