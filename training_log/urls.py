from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log_session, name='log-session'),
    path('log-details/', views.log_details, name='log-details')
]