from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


def contact(request):
    """
    Handle contact form submission.

    Renders the contact form page and processes form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_success_email(form.cleaned_data['email'])
            return redirect('contact_form_success')
        else:
            messages.error(
                request, 'An error occured. Please try again.')
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})


def contact_form_success(request):
    """
    Render the contact success page.
    """
    return render(request, 'contact/contact_form_success.html')


def send_contact_success_email(user_email):
    """
    Send a confirmation email to the user \
    upon successful contact form submission.

    Args:
        user_email (str): The email address of the user \
        who submitted the contact form.
    """
    subject = 'Contact Form Received'
    message_body = "Thank you for contacting us! \
                    We will get back to you as soon as possible!"
    signature = "\n\nSincerely yours,\nTrack My Job!"
    message = f"{message_body}{signature}"
    from_email = 'viola.bergere@gmail.com'
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')
