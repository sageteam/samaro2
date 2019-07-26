from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedRelatedField
from trip.models import Seat
from trip.models import Trip

from .city import CitySerializer
from .region import RegionSerializer
from .users import UserSerializer

class SeatSerializer(ModelSerializer):

    class Meta:
        model = Seat
        fields = ('id', 'position', 'state', 'init_price', 'paid_price', 'type_price', 'discount', 'user', 'trip')
        # read_only_fields = ('trip', 'position')

class TripSerializer(ModelSerializer):
    origin = CitySerializer(required = True)
    destination = CitySerializer(required = True)
    origin_region = RegionSerializer(required = True)
    destination_region = RegionSerializer(required = True)
    seat = SeatSerializer(required = True, many = True)
    
    driver = UserSerializer(required = True)

    class Meta:
        model = Trip
        fields = ('pk', 'origin', 'origin_region', 'destination', 'destination_region', 'driver', 'seat', 'status', 'gender', 'active', 'start_time', 'type_creator', 'front_seat_price', 'back_seat_price')
        read_only_fields = ('seat', )

class TripMainSerializer(ModelSerializer):
    
    class Meta:
        model = Trip
        fields = ('pk', 'origin', 'origin_region', 'destination', 'destination_region', 'driver', 'status', 'gender', 'active', 'start_time', 'type_creator', 'front_seat_price', 'back_seat_price')

