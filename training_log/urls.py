from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('log/', views.log_session, name='log-session'),
    path('log-details/', views.log_details, name='log-details'),
    path('training_log/<int:pk>/', views.TrainingLogDetail.as_view(), name='training_log-detail'),
    path('training_log/<int:pk>/update', views.TrainingLogUpdate.as_view(), name='training_log-update'),
    path('training_log/<int:pk>/delete', views.TrainingLogDelete.as_view(), name='training_log-delete')
]