from django.shortcuts import render
from .models import FAQ


def home(request):
    return render(request, 'home/index.html')


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "home/faq.html", {'faqs': faqs})


def privacy_policy(request):
    """ A view to return the Privacy Policy page"""

    return render(request, "home/privacy_policy.html")

def team_page(request):
    return render(request, "home/team_page.html")
