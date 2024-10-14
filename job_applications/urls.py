from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_applications, name='job_applications'),
    path('job/edit/<int:job_id>/', views.edit_application, name='edit_application'),
    
]
