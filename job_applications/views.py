from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import JobApplication
from .forms import JobApplicationForm


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
