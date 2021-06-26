from django.urls import path
from . import views

urlpatterns = [
    path('log-test/', views.log_test, name='log-test'),
    path('charts/', views.line_chart, name='chart'),
    path('chartsJSON', views.line_chart_json, name='line_chart_json')
]