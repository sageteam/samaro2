import secrets 
import khayyam
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from trip.models import Trip
from .models import TicketLetter
from .models import TicketEnvelope
from rest_framework.exceptions import NotAcceptable

@receiver(pre_save, sender=TicketLetter)
def create_ticket_letter_pre_save(sender, instance, *args, **kwargs):
    passenger = None
    driver = None
    if instance.reply:
        passenger = instance.reply.passenger
        driver = instance.reply.driver    
        END = 2
        if instance.reply.trip.status == END:
            raise Exception('Trip is Ended. We can\'t send your message')
    
    
    instance.sku = secrets.token_hex(3)


@receiver(pre_save, sender=TicketEnvelope)
def create_ticket_envelope_pre_save(sender, instance, *args, **kwargs):
    driver_has_active_trip = Trip.objects.has_active_trip(instance.driver)
    if not driver_has_active_trip:
        raise NotAcceptable('Driver trip\'s is not active')
    
    # check driver is not a passenger
    if instance.driver == instance.passenger:
        raise NotAcceptable('Conversation can not between one person!')
    
    # check each passenger has just one ticket.
    tickets = TicketEnvelope.objects.filter(trip = instance.trip)
    if not instance.pk:
        for ticket in tickets:
            if ticket.passenger == instance.passenger:
                raise NotAcceptable('Active conversation is now available')

        
        # check tickets reach to 4
        if len(tickets) == 4:
            raise NotAcceptable('Now, 4 tickets are available, you can\'t create more envelope.')

        today = khayyam.JalaliDatetime.now().strftime('%y%m%d')
        security_code = secrets.token_hex(3)
        instance.sku = '{}{}'.format(today, security_code)

    END = 2
    if instance.trip.status == END:
        raise Exception('Trip is Ended. We can\'t send your message')


@receiver(post_save, sender=TicketEnvelope)
def create_ticket_envelope_post_save(sender, instance, created, *args, **kwargs):
    # Send Email each time TicketEnvelope created
    # Send Email to driver
    # Send Email to passenger
    pass