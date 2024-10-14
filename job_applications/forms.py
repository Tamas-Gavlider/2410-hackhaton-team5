from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company_name', 'position', 'location', 'salary', 'employment_type',
            'application_date', 'status', 'job_description', 'application_deadline',
            'contact_person', 'contact_email', 'application_method', 'interview_date',
            'notes'
        ]
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }
