from trip.models import Region, City
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField

class RegionSerializer(ModelSerializer):
    city = SlugRelatedField(queryset = City.objects.all(), slug_field='name')
    class Meta:
        model = Region
        fields = ('id', 'name', 'city', 'is_traditional')
