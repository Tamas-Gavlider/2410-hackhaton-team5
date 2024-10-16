from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_job_applications_view, name='job_applications'),
    path('job/<int:job_id>/', views.application_detail, name='application_detail'),
    path('job/add/', views.add_application, name='add_application'),
    path('job/delete/<int:job_id>/', views.delete_application, name='delete_application'),
    path('job/edit/<int:job_id>/', views.edit_application, name='edit_application'),
]
