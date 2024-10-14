from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing contact messages.

    Attributes:
        list_display: Fields to be displayed in the list view.
    """

    list_display = ('message', 'read',)
