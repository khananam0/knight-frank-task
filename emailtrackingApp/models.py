from django.db import models

# Create your models here.

class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipients = models.TextField()  # Comma-separated list of email addresses
    sent_at = models.DateTimeField(null=True, blank=True)
    opened_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.recipients
    




