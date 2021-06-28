from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



@receiver(post_save, sender=User) # whenever an instance the sender class is created, send the below signal:
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #instance refers to the User object created


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# DO NOT FORGET TO IMPORT SIGNALS IN APPS.PY!!!!!    