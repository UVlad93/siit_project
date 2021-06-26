from django.shortcuts import render, redirect
from .forms import TestingSessionForm
from .models import TestingSession
from django.contrib import messages
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


# Create your views here.

def log_test(request):
    if request.method =='POST':
        form = TestingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your assessment has been added to your profile')
            return redirect('home')
    else:
        form = TestingSessionForm()
    return render(request, 'training_log/log_test.html', {'form': form})    

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        dates = []
        qs = TestingSession.objects.all()
        for test in qs:
            dates.append(test.date_logged)
        return dates    

    def get_providers(self):
        return ["MH-MAW", "PU-MAW", "FL"]
            

    def get_data(self):
        mh_results = []
        pu_results = []
        fl_results = []
        qs = TestingSession.objects.all()
        for test in qs:
            mh_results.append(test.mh_maw)
            pu_results.append(test.pu_maw)
            fl_results.append(test.fl)
        results = [mh_results] + [pu_results] + [fl_results]   
        return results   

line_chart = TemplateView.as_view(template_name='training_log/charts.html')
line_chart_json = LineChartJSONView.as_view()
