from django.db.models import query
from django.db.models import Manager

class TripModelQuerySet(query.QuerySet):
    def driver_pending_trips(self, value):
        PENDING = 1
        return self.filter(driver = value).filter(status = PENDING)
    
    def active(self, value):
        return self.filter(active = value)
    
    
    def type_creator(self, value):
        return self.filter(type_creator = value)
    
class TripModelManager(Manager):
    def get_queryset(self):
        return TripModelQuerySet(self.model, using=self._db)
    
    def has_active_trip(self, value):
        if value == None:
            return False
        result = self.get_queryset().driver_pending_trips(value)
        return True if any(result) else False
    
    def passenger_has_active_trip(self, value):
        if value == None:
            return False
        trips = self.get_queryset().active(True)
        for trip in trips:
            for seat in trip.seat.all():
                if seat.user.pk == value:
                    return True
        return False
    

    def get_active_trips(self, value):
        return self.get_queryset().filter(driver = value).active(True)
    
    def get_previous_trips(self, value):
        return self.get_queryset().filter(driver = value).active(False).filter(state = 1)

    def get_aborted_trips(self, value):
        return self.get_queryset().filter(driver = value).active(False).filter(state = 2)
    
    def get_active_trips_passenger(self, value):
        return self.get_queryset().active(True).filter(seat__user = value)
    
    def get_previous_trips_passenger(self, value):
        return self.get_queryset().active(False).filter(state = 1).filter(seat__user = value)
    
    def get_aborted_trips_passenger(self, value):
        return self.get_queryset().active(False).filter(state = 0).filter(seat__user = value)

    def get_trips(self, value):
        return self.get_queryset().active(True).type_creator(value)

    def all(self, *args, **kwargs):
        # All active trips
        return self.get_queryset().active(True)
