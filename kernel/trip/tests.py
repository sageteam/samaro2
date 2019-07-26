from django.test import TestCase
from django.utils import timezone as tz
from django.db.models import Count
from .models import Trip, Seat
from .models import City, Region
from accounts.models import User
from django.db.utils import IntegrityError

# Create your tests here.
class TripModel(TestCase):
    def setUp(self):
        self.city1 = City.objects.create(name = 'Nowshahr')
        self.city2 = City.objects.create(name = 'Tehran')
        self.region1 = Region.objects.create(name = 'Homafaran', city = self.city1)
        self.region2 = Region.objects.create(name = 'TehranPars', city = self.city2)
        
        self.city3 = City.objects.create(name = 'Ahvaz')
        self.false_region = Region.objects.create(name = 'TehranPars', city = self.city2)
        
        self.user = User.objects.create(email = 'sa.goldeneagle@gmail.com', password = 'sepehr1234')
        self.trip = Trip.objects.create(
            start_time = tz.now(), 
            end_time = tz.now(), 
            origin = self.city1, 
            destination = self.city2, 
            origin_region = self.region1,
            destination_region = self.region2,
            driver = self.user,
            status = 1
            )

    def test_trip_creation(self):
        self.assertIsNotNone(self.trip.seat)
    
    def test_trip_four_seats(self):
        seats = Trip.objects.aggregate(count = Count('seat'))
        self.assertEqual(seats['count'], 4)
    
    def test_driver_has_active_trip(self):
        self.assertTrue(Trip.objects.has_active_trip(self.trip.driver))
    
    def test_just_one_active_trip(self):
        with self.assertRaises(ValueError):
            self.trip = Trip.objects.create(
                start_time = tz.now(), 
                end_time = tz.now(), 
                origin = self.city1, 
                destination = self.city2, 
                origin_region = self.region1,
                destination_region = self.region2,
                driver = self.user,
                status = 1
            )

    def test_region_subset_of_city(self):
        with self.assertRaises(ValueError):
            self.trip = Trip.objects.create(
                start_time = tz.now(), 
                end_time = tz.now(), 
                origin = self.city1, 
                destination = self.city2, 
                origin_region = self.false_region,
                destination_region = self.false_region,
                driver = self.user,
                status = 1
            )
