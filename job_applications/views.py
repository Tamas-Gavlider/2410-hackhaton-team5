from django.shortcuts import render


def dashboard(request):
    return render(request, 'job_applications/dashboard.html')
