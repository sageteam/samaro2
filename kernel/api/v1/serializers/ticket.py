from rest_framework.serializers import ModelSerializer

from ticket.models import TicketEnvelope
from ticket.models import TicketLetter

class TicketEnvelopeSerializer(ModelSerializer):
    class Meta:
        model = TicketEnvelope
        fields = ('sku', 'subject', 'priority', 'status', 'department', 'trip', 'passenger', 'driver')

class TicketLetterSerializer(ModelSerializer):
    class Meta:
        model = TicketLetter
        fields = ('message', 'ticket', 'user', 'reply')