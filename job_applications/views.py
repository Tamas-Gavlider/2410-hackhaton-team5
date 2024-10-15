from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import JobApplication
from .forms import JobApplicationForm


@login_required
def user_job_applications_view(request):

    user_applications = JobApplication.objects.filter(user=request.user)

    context = {
        'applications': user_applications
    }

    return render(request, 'job_applications/job_applications.html', context)


@login_required
def edit_application(request, job_id):

    job = get_object_or_404(JobApplication, pk=job_id, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')  # Temporarily until dashboard is ready !!!
    else:
        form = JobApplicationForm(instance=job)

    context = {
        'job': job,
        'form': form,
    }

    return render(request, 'job_applications/edit-application.html', context)


@login_required
def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.save()
            return redirect('home')  # Temporarily until dashboard is ready !!!
    else:
        form = JobApplicationForm()

    context = {
        'form': form,
    }

    return render(request, 'job_applications/add-application.html', context)


@login_required
def delete_application(request, job_id):

    job = get_object_or_404(JobApplication, id=job_id, user=request.user)

    job.delete()

    return redirect('home')  # Update this to your dashboard or list view when ready
