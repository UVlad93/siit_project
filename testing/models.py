from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TestingSession(models.Model):
    name = models.CharField(max_length=100, help_text="Choose a title for your testing session")
    mh_maw = models.IntegerField(help_text='Max Hangs- Maximum Added Weight (in kg)')
    pu_maw = models.IntegerField(help_text='Maximum Added Weight Pull Up (in kg)')
    fl = models.IntegerField(help_text='Maximum Front Lever Hold (in seconds)')
    date_logged = models.DateField(default=timezone.now, help_text='Date Logged')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}: {self.mh_maw}, {self.pu_maw}, {self.fl}- {self.date_logged}"

