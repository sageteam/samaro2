from django.contrib import admin
from khayyam import JalaliDatetime as jd
from .models import Distance
from .models import City
from .models import Region
from .models import Seat
from .models import Trip

class SeatInline(admin.TabularInline):
    model = Seat
    fields = ['position', 'state', 'init_price', 'paid_price', 'type_price', 'discount', 'user', 'trip']
    extra = 1

class RegionInline(admin.TabularInline):
    model = Region
    fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for Region'''

    list_display = ('name', 'Modified')
    list_filter = ('modified',)

    search_fields = ('name',)

    inlines = [
        RegionInline,
    ]

    def Modified(self, obj):
        p_date = jd(obj.modified).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.modified).strftime('%Q')
        return e_date

class AcrossCitiesInline(admin.TabularInline):
    model = City
    fields = ['name', 'across']

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    '''Admin View for Distance'''

    list_display = ('url', 'road', 'distance', 'active', 'price', 'Modified')
    list_filter = ('active',)
    inlines = [
        # AcrossCitiesInline,
    ]
    raw_id_fields = ('city1', 'city2')
    readonly_fields = ('price', 'url')
    search_fields = ('url', 'road')
    ordering = ('-modified',)


    def Modified(self, obj):
        p_date = jd(obj.modified).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.modified).strftime('%Q')
        return e_date


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    '''Admin View for Trip'''

    list_display = ('Trip', 'driver', 'status', 'gender', 'active', 'Date', 'state', 'type_creator', 'is_dispatcher')
    list_filter = ('start_time', 'status' , 'gender', 'active', 'is_dispatcher', 'type_creator', 'state')
    raw_id_fields = ('origin', 'destination')
    search_fields = ('origin', 'destination', 'driver')
    ordering = ('status', 'active', '-created')
    inlines = (SeatInline,)

    def Trip(self, obj):
        return '{}-{}'.format(obj.origin, obj.destination)

    def Created(self, obj):
        p_date = jd(obj.created).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.created).strftime('%Q')
        return e_date

    def Date(self, obj):
        p_date = jd(obj.created).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.created).strftime('%Q')
        return e_date
    
    # def get_readonly_fields(self, request, obj = None):
    #     return [f.name for f in self.model._meta.fields] 