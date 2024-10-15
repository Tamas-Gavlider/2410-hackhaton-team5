from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from job_applications.models import JobApplication


@login_required
def dashboard(request):

    user = request.user

    job_applications = JobApplication.objects.filter(user=user)

    total_applications = job_applications.count()

    status_filter = request.GET.get('status')
    employment_type_filter = request.GET.get('employment_type')

    if status_filter:
        job_applications = job_applications.filter(status=status_filter)

    if employment_type_filter:
        job_applications = job_applications.filter(employment_type=employment_type_filter)

    sort_by = request.GET.get('sort_by', 'draft_created')  # Default sort by draft_created
    direction = request.GET.get('direction', 'desc')

    # Toggle direction
    if direction == 'asc':
        order_by = sort_by
        new_direction = 'desc'
    else:
        order_by = f'-{sort_by}'
        new_direction = 'asc'

    job_applications = job_applications.order_by(order_by)
    total_applications_filtered = job_applications.count()

    context = {
        'job_applications': job_applications,
        'status_choices': JobApplication.STATUS_CHOICES,
        'employment_type_choices': JobApplication.EMPLOYMENT_TYPES,
        'new_direction': new_direction,
        'total_applications': total_applications,
        'total_applications_filtered': total_applications_filtered,
    }

    return render(request, 'dashboard/dashboard.html', context)
