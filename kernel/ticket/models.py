import secrets
import khayyam

from accounts.models import User
from trip.models import Trip
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class TicketEnvelope(models.Model):
    PRIORITY_CHOICES = ((4, _("Urgent")),
                        (3, _("High")),
                        (2, _("Medium")),
                        (1, _("Low"))
                        )
    STATUS_CHOICES = (
        (1, _("Open")),
        (0, _("Suspended")),
        (-1, _("Close")),
    )

    sku = models.CharField(max_length = 15, editable = False, primary_key = True)
    
    subject = models.CharField(max_length=150, verbose_name=_('Subject'))
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=1)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
    department = models.ForeignKey('Department', on_delete = models.SET_NULL, related_name='tickets', null = True, verbose_name=_('department'))
    
    trip = models.ForeignKey(Trip, on_delete = models.SET_NULL, null = True, related_name='envelope', verbose_name = _('trip'))
    passenger = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name='ticket_passenger', verbose_name=_('Passenger'))
    driver = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name='ticket_driver', verbose_name=_('Driver'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['-created']

    def __str__(self):
        return self.sku


class TicketLetter(models.Model):
    sku = models.CharField(max_length = 15, editable = False, primary_key = True)
    
    message = models.TextField(verbose_name=_('Message'))
    ticket = models.ForeignKey('TicketEnvelope', on_delete = models.CASCADE, related_name='messages', verbose_name = _('Ticket'))
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name='letter_user', verbose_name=_('Letter user'))
    reply = models.ForeignKey('TicketEnvelope', on_delete = models.CASCADE, null = True, related_name='letter_reply', verbose_name=_('Reply'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['-created']
    
    def __str__(self):
        return "{} - {}".format(self.sku, self.user)


class Department(models.Model):
    title = models.CharField(max_length = 32, verbose_name=_('title'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
    
    def __str__(self):
        return self.title
    
