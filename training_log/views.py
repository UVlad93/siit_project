from .forms import TrainingLogCompleteForm, TrainingLogSessionForm
from django.shortcuts import render, redirect
from .models import SessionType, TrainingLog, Exercise
from django.contrib import messages
from django import forms

# Create your views here.

def home(request):
    ctxt = {
        'logs': TrainingLog.objects.all()
    }
    return render(request, 'training_log/home.html', ctxt)


def log_session(request):
    if request.method == 'POST':
        form = TrainingLogSessionForm(request.POST)
        if form.is_valid():
            request.session['session_type'] = request.POST['session_type']       
            return redirect('log-details')  
        else:
            messages.error(request, 'Oupsie')
    else:
        form = TrainingLogSessionForm()
        return render(request, 'training_log/log_session.html', {'form':form}) 


def log_details(request):
    session = request.session['session_type']
    qs = Exercise.objects.filter(session_type__name=session)
    TrainingLogCompleteForm.base_fields['exercises'] = forms.ModelMultipleChoiceField(
                                    queryset=qs, widget=forms.CheckboxSelectMultiple)                                                              
    form = TrainingLogCompleteForm() 

    if request.method == 'POST':
        form = TrainingLogCompleteForm(request.POST)
        if form.is_valid():
            #session_type = SessionType.objects.get(name=request.session['session_type'])
            exs = form.cleaned_data['exercises']
            form.fields['exercises']=exs
            form.instance.author = request.user
            date_posted = form.cleaned_data['date_posted']
            #tlog= TrainingLog.objects.create(session_type=session_type, date_posted=date_posted)

            messages.success(request, 'Your training session has been added to your logbook') 
            return redirect('home') 
    else:
        form = TrainingLogCompleteForm()
    return render(request, 'training_log/log_details.html', {'form':form})                                       



