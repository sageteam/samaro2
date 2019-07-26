from trip.models import Distance
from trip.models import City
from django_filters import rest_framework as filters
from .city import CitySerializer
from .region import RegionSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField


class DistanceSerializer(ModelSerializer):
    city1 = SlugRelatedField(queryset = City.objects.all(), slug_field='name')
    city2 = SlugRelatedField(queryset = City.objects.all(), slug_field = 'name')
    across = SlugRelatedField(queryset = City.objects.all(), many = True, slug_field='name')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city1', 'city2')

    class Meta:
        model = Distance
        fields = ('url', 'city1', 'city2', 'across', 'road', 'price', 'distance')
        read_only_fields = ('url', 'price', 'across')
        
