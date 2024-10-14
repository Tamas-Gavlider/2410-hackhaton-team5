from django.urls import path
from . import views
from .views import contact


urlpatterns = [
  path('contact/', contact, name='contact'),
  path(
     'contact_form_success/',
     views.contact_form_success,
     name='contact_form_success'),
]
