from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ReturnDict

from django_filters import rest_framework as filters

##################
###### User ######
##################
from accounts.models import User
from .serializers.users import UserSerializer
from .serializers.users import UserRegisterSerializer
# Profile
from users.models import GeneralProfile
from .serializers.users import UserProfileSerializer
# Favorites
from users.models import Favorites
from .serializers.users import UserFavoritesSerializer
# Setting
from users.models import Setting
from .serializers.users import UserSettingSerializer
# Driver
from users.models import Driver
from .serializers.users import UserProfileDriverSerializer
# Machine
from users.models import Machine
from .serializers.users import MachineSerializer
# Bank
from users.models import Bank
from .serializers.users import BankSerializer
# Bank
from users.models import Passenger
from .serializers.users import UserProfilePassengerSerializer
# Bank
from users.models import Transmit
from .serializers.users import UserProfileTransmitSerializer
# Feature
from users.models import Feature
from .serializers.users import MachineFeaturesSerializer

##################
###### Trip ######
##################
# City
from trip.models import City
from .serializers.city import CitySerializer
# Region
from trip.models import Region
from .serializers.region import RegionSerializer
# City
from trip.models import Distance
from .serializers.distance import DistanceSerializer
# trip
from trip.models import Trip
from .serializers.trip import TripMainSerializer
from .serializers.trip import TripSerializer

from trip.models import Seat
from .serializers.trip import SeatSerializer

##################
###### Trip ######
##################
class APITripListCreate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        trips = Trip.objects.all()
        serializer = TripMainSerializer(trips, many = True)
        return Response(serializer.data)

    
    def post(self, request, format = None, *args, **kwargs):
        serializer = TripMainSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APITripRetrieveUpdate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        serializer = TripMainSerializer(trip)
        return Response(serializer.data)
    
    def put(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        serializer = TripMainSerializer(trip, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound
        
class APIAllTripsUser(APIView):
    
    def get(self, request, format = None, *args, **kwargs):
        seats = Seat.objects.filter(user = self.request.user)
        trips = [Trip.objects.get(trip = seat.trip) for seat in seats]
        serializer = TripMainSerializer(trips, many = True)
        return Response(serializer.data)

class APISeatsATrip(APIView):
    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seats = Seat.objects.filter(trip = trip)
        serializer = SeatSerializer(seats, many = True)
        return Response(serializer.data)

    
    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound
    
    def post(self, request, format = None, *args, **kwargs):
        serializer = SeatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class APISeatsATripUpdate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seat = Seat.objects.filter(trip = trip, position = kwargs['pos'])[0]

        serializer = SeatSerializer(seat)

        return Response(serializer.data)

    def put(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seat = Seat.objects.filter(trip = trip, position = kwargs['pos'])[0]
        # print(seat)
        serializer = SeatSerializer(seat, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound

##################
##### Ticket #####
##################
from .serializers.ticket import TicketEnvelopeSerializer
from ticket.models import TicketEnvelope
from .serializers.ticket import TicketLetterSerializer
from ticket.models import TicketLetter

##################
### Dashboard ####
##################
from dashboard.models import Rules
from .serializers.dashboard import RulesSerializer
from dashboard.models import RulesCategory
from .serializers.dashboard import RulesCategorySerializer
from dashboard.models import FAQ
from .serializers.dashboard import FAQSerializer
from dashboard.models import FAQCategory
from .serializers.dashboard import FAQCategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class APIRetrieveUpdateUserProfile(generics.RetrieveUpdateAPIView):
    queryset = GeneralProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class APIFavoites(APIView):
    # permission_classes = (UserPermission,)

    def get(self, request, format = None, *args, **kwargs):
        user_pk = kwargs['user']
        favorites = Favorites.objects.filter(user = user_pk)
        serializer = UserFavoritesSerializer(favorites, many = True)
        
        try:
            obj = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            # return Response({'NotFound': 'User Queryset does not match.'})
            raise PermissionDenied

        return Response(serializer.data)
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = UserFavoritesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class APIFavoritesUpdate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        # self.check_permission(self.request.user, user)
        favorite = self.get_object(user, kwargs['title'])
        serializer = UserFavoritesSerializer(favorite)
        return Response(serializer.data)
    
    def get_user(self, user_pk, *args, **kwargs):
        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise PermissionDenied

    def get_object(self, user_pk, favorite_title, *args, **kwargs):
        try:
            return Favorites.objects.filter(user = user_pk).filter(title = favorite_title)[0]
        except IndexError:
            raise NotFound
    
    # def check_permission(self, request_user, user):
    #     # Permission check
    #     if not user == request_user:
    #         raise PermissionDenied

    def put(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
    
        # self.check_permission(request.data['user'], user.pk)
        favorite = self.get_object(user, kwargs['title'])
        serializer = UserFavoritesSerializer(favorite, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        # self.check_permission(self.request.user.pk, user.pk)
        favorite = self.get_object(user, kwargs['title'])
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class APIRetrieveUpdateUserProfileDriver(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = UserProfileDriverSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserMachine(generics.RetrieveUpdateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    lookup_field = 'driver'
    lookup_url_kwarg = 'driver'

class APIRetrieveUpdateUserBank(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'driver'
    lookup_url_kwarg = 'driver'

class APIRetrieveUpdateUserProfilePassenger(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = UserProfilePassengerSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserProfileTransmit(generics.RetrieveUpdateAPIView):
    queryset = Transmit.objects.all()
    serializer_class = UserProfileTransmitSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = MachineFeaturesSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

######## Ticket ########
class TicketViewSet(viewsets.ModelViewSet):
    queryset = TicketEnvelope.objects.all()
    serializer_class = TicketEnvelopeSerializer
    lookup_field = 'sku'
    lookup_url_field = 'sku'

class TicketLetterViewSet(viewsets.ModelViewSet):
    queryset = TicketLetter.objects.all()
    serializer_class = TicketLetterSerializer
    lookup_field = 'sku'
    lookup_url_field = 'sku'

######## City ########
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


######## Region ########
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


######## DISTANCE ########
class DistanceViewSet(viewsets.ModelViewSet):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer
    lookup_field = 'road'
    lookup_url_kwarg = 'road'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city1', 'city2', 'road')

######## Dashboard ########
class RulesViewSet(viewsets.ModelViewSet):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class RulesCategoryViewSet(viewsets.ModelViewSet):
    queryset = RulesCategory.objects.all()
    serializer_class = RulesCategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class FAQCategoryViewSet(viewsets.ModelViewSet):
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

#### Authentication

class APILoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)

class APIRegister(APIView):
    def post(self, request, format = None, *args, **kwargs):
        
        serializer = UserRegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
