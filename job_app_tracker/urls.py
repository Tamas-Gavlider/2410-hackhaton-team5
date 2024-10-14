from django.contrib import admin
from django.urls import path, include

from . views import error_403, error_404, error_500


handler403 = error_403
handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('job_applications/', include('job_applications.urls')),
    path('', include('contact.urls')),
]
