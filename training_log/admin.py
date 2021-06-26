from django.contrib import admin
from .models import SessionType, Exercise, TrainingLog

# Register your models here.
admin.site.register(SessionType)
admin.site.register(Exercise),
admin.site.register(TrainingLog)
