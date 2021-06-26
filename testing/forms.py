from .models import TestingSession
from django import forms

class TestingSessionForm(forms.ModelForm):
    class Meta:
        model = TestingSession
        fields = '__all__'