from django.db import models
from django.shortcuts import reverse

from django.utils import timezone


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Requests'

    SUBJECTS = (
        ('Order Inquiry', 'Order Inquiry'),
        ('Custom Inquiry', 'Custom Inquiry'),
        ('Press Inquiry', 'Press Inquiry'),
        ('Account Issues', "Account Issues"),
        ('Other', "Other"),
    )

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(choices=SUBJECTS, max_length=254,)
    message = models.TextField(max_length=1024)
    date_created = models.DateTimeField(default=timezone.now)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.email
