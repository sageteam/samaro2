from accounts.models import User
from users.models import Feature
from users.models import Bank
from users.models import GeneralProfile
from users.models import Driver
from users.models import Setting
from users.models import Notifications
from users.models import Favorites
from users.models import Passenger
from users.models import Transmit
from users.models import Machine

from rest_framework.exceptions import NotAcceptable
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField


#######################
### User Serializer ###
####################### 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'profile', 'favorites', 'setting')
        depth = 1

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = GeneralProfile
        fields = ('gender', 'credit', 'birth_date', 'national_code', 'tel', 'mobile', 'adr', 'postal_code', 'pic', 'national_code_pic', 'edu_degree', 'about', 'driver', 'transmit', 'passenger')
        read_only_fields = ('credit',)
        depth = 1

class UserSettingSerializer(ModelSerializer):
    
    class Meta:
        model = Setting
        fields = ('get_message_from', 'subscribe', 'email_transaction', 'email_trip_info')

class UserFavoritesSerializer(ModelSerializer):
    
    class Meta:
        model = Favorites
        fields = ('title', 'status', 'user')

class UserProfileDriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ('job', 'score', 'job_place', 'emergency_number', 'machine', 'bank')
        # read_only_fields = ('score',)
        depth = 1

class MachineSerializer(ModelSerializer):
    features = SlugRelatedField(queryset = Feature.objects.all(), many = True, slug_field = 'name')

    class Meta:
        model = Machine
        fields = ('name', 'color', 'model', 'plaque', 'year', 'chassis_number', 'driver_card', 'machine_card', 'misdiagnosis', 'car_pic', 'features')

class MachineFeaturesSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = ('name', 'status')


class BankSerializer(ModelSerializer):

    class Meta:
        model = Bank
        fields = ('bank_acc_name', 'bank_name', 'bank_sheba', 'bank_card')

class UserProfilePassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('score', 'job', 'emergency_number')
        # read_only_fields = ('score',)

class UserProfileTransmitSerializer(ModelSerializer):

    class Meta:
        model = Transmit
        fields = ('score', 'job', 'emergency_number')
        # read_only_fields = ('score',)
