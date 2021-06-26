from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SessionType(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name}"

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    session_type = models.ForeignKey(SessionType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"         

class TrainingLog(models.Model):
    session_type = models.ForeignKey(SessionType, on_delete=models.CASCADE, null=True)
    exercises = models.ManyToManyField(Exercise)
    comments = models.TextField(max_length=500)
    date_posted = models.DateField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.session_type}- {self.date_posted}- {self.exercises}"