from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Group(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name='groups')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

