from .models import TestingSession
from django import forms

class TestingSessionForm(forms.ModelForm):
    class Meta:
        model = TestingSession
        fields = ['name', 'mh_maw', 'pu_maw', 'fl', 'date_logged']

    def form_valid(self, form):   
        form.instance.author = self.request.user
        return super().form_valid(form)     