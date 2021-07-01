from .forms import TrainingLogCompleteForm, TrainingLogSessionForm
from django.shortcuts import render, redirect
from .models import SessionType, TrainingLog, Exercise
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render (request, 'training_log/about.html')

@login_required
def home(request):
    ctxt = {
        'logs': TrainingLog.objects.filter(author=request.user)
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
            session_type = SessionType.objects.get(name=request.session['session_type'])
            exs = form.cleaned_data['exercises']
            date_posted = form.cleaned_data['date_posted']
            comments = form.cleaned_data['comments']
            tlog = TrainingLog.objects.create(session_type=session_type, comments=comments, 
                                            date_posted=date_posted, author=request.user)                                
            for ex in exs:
                obj = Exercise.objects.get(name=str(ex))
                print(obj)
                tlog.exercises.add(obj)
            tlog.save()
            messages.success(request, 'Your training session has been added to your logbook') 
            return redirect('home') 
    else:
        form = TrainingLogCompleteForm()
    return render(request, 'training_log/log_details.html', {'form':form})                                       



