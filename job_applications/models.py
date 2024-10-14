from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Interview appointed', 'Interview appointed'),
        ('Interviewed', 'Interviewed'),
        ('Offered', 'Offered'),
        ('Offer accepted', 'Offer accepted'),
        ('Rejected', 'Rejected'),
    ]
    EMPLOYMENT_TYPES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Contract', 'Contract'),
        ('Temporary', 'Temporary'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Office-based', 'Office-based'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Project-based', 'Project-based'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES, default='Full time')
    draft_created = models.DateTimeField(auto_now_add=True)
    application_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft')
    job_description = models.TextField(blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    application_method = models.CharField(max_length=100, blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"
