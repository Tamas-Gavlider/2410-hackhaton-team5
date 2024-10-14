from django.db import models


# Contact model
class Contact(models.Model):
    """
    Represents a contact form submission.

    Attributes:
        first_name (CharField): The first name \
        of the person submitting the form.
        last_name (CharField): The last name \
        of the person submitting the form.
        email (EmailField): The email address \
        of the person submitting the form.
        message (TextField): The message submitted through the form.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"
