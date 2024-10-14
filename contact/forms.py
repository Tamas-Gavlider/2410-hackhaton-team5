from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for capturing contact information.

    Attributes:
        first_name (CharField): The first name \
        of the person submitting the form.
        last_name (CharField): The last name \
        of the person submitting the form.
        email (EmailField): The email address \
        of the person submitting the form.
        message (TextField): The message submitted through the form.
    """
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email address',
            'message': 'Message',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                    'autocomplete': 'name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                    'autocomplete': 'family-name'
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email',
                    'autocomplete': 'email'
                }),
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter your message here'}),
        }
