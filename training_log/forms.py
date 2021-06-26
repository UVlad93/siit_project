from django import forms
from .models import Exercise, SessionType, TrainingLog

class TrainingLogSessionForm(forms.Form):
    session_types = [session.name for session in SessionType.objects.all()]
    sessions = tuple(zip(session_types, session_types))
    session_type = forms.MultipleChoiceField(choices = sessions)
    

class TrainingLogCompleteForm(forms.ModelForm):

    class Meta:
        model = TrainingLog
        fields = ['exercises', 'comments', 'date_posted'] 

    




