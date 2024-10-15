from collections import Counter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
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
        job_applications = job_applications.filter(
            employment_type=employment_type_filter)

    # Default sort by draft_created
    sort_by = request.GET.get('sort_by', 'draft_created')
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

    # Data for Charts
    status_count = dict(
        Counter(job_applications.values_list('status', flat=True)))
    employment_type_count = dict(
        Counter(job_applications.values_list('employment_type', flat=True)))

    # Data for Applications Over Time
    now = timezone.now()
    last_week_count = JobApplication.objects.filter(
        user=user, application_date__gte=now - timedelta(days=7)).count()
    last_month_count = JobApplication.objects.filter(
        user=user, application_date__gte=now - timedelta(days=30)).count()
    last_six_months_count = JobApplication.objects.filter(
        user=user, application_date__gte=now - timedelta(days=180)).count()

    context = {
        'job_applications': job_applications,
        'status_choices': JobApplication.STATUS_CHOICES,
        'employment_type_choices': JobApplication.EMPLOYMENT_TYPES,
        'new_direction': new_direction,
        'total_applications': total_applications,
        'total_applications_filtered': total_applications_filtered,
        'status_count': status_count,
        'employment_type_count': employment_type_count,
        'applied_counts': {
            'last_week': last_week_count,
            'last_month': last_month_count,
            'last_six_months': last_six_months_count,
        },
    }

    return render(request, 'dashboard/dashboard.html', context)
