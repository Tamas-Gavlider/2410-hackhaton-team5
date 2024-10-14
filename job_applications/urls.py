from django.urls import path
from . import views

urlpatterns = [
    path('job/edit/<int:job_id>/', views.edit_application, name='edit_application'),
]
