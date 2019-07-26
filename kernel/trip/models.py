import secrets

from accounts.models import User
from datetime import timedelta
from .validations import validate_region_subset_of_city

from trip.querysets import TripModelManager

from django.db.models import Q, Count
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class City(models.Model):
    name = models.CharField(max_length = 64, unique = True, verbose_name = _('name'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return smart_text(self.name)

class Region(models.Model):
    name = models.CharField(max_length = 64)
    is_traditional = models.BooleanField(default = False)

    city = models.ForeignKey('City', on_delete = models.CASCADE, related_name='regions')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return smart_text("{} -> {}".format(self.city.name, self.name))

class Distance(models.Model):
    city1 = models.ForeignKey('City', on_delete=models.CASCADE, related_name='city1')
    city2 = models.ForeignKey('City', on_delete=models.CASCADE, related_name='city2')
    road = models.CharField(max_length = 128, unique = True, verbose_name = _('road'))
    url = models.SlugField(max_length = 128, verbose_name = _('slug'), help_text = _('url accessibilty'))
    across = models.ManyToManyField('City', related_name='distance')
    distance = models.PositiveIntegerField(default = 0, null = False, blank = False, help_text=_("based on kilometer."))

    price = models.PositiveIntegerField(default = 0)

    active = models.BooleanField(default = True, help_text = _('if you want to deactivate this road, please make it false.'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Distance')
        verbose_name_plural = _('Distances')
        indexes = [
            models.Index(fields=['url'])
        ]
    
    def save(self, *args, **kwargs):
        self.url = f"{self.city1}-{self.city2}"
        if not self.road:
            self.road = f"{self.city1}-{self.city2}"

        
        super(Distance, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.city1, self.city2)

class Seat(models.Model):
    STATES = (
        (1, _('singular')),
        (2, _('plural'))
    )

    POSITIONS = (
        (1, _('front seat')),
        (2, _('left seat')),
        (3, _('middle seat')),
        (4, _('right seat'))
    )

    PAYMENTS = (
        (1, _('cash')),
        (2, _('online'))
    )

    position = models.PositiveSmallIntegerField(choices=POSITIONS, null = True, verbose_name=_('position'))
    state = models.PositiveSmallIntegerField(choices=STATES, null = True, verbose_name=_('state'))
    init_price = models.PositiveIntegerField(null = True, verbose_name=_('price'))
    paid_price = models.PositiveIntegerField(null = True, verbose_name=_('paid_price'))
    type_price = models.SmallIntegerField(null = True, choices = PAYMENTS, default = 2)
    discount = models.CharField(max_length = 64, null = True, verbose_name = _('discount'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, verbose_name=_('user'))
    trip = models.ForeignKey('Trip', on_delete = models.CASCADE, related_name='seat', null = True, verbose_name=_('trip'))

    def save(self, *args, **kwargs):

        # trip = Trip.objects.aggregate(count = Count('trip'))

        super(Seat, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Seat')
        verbose_name = _('Seats')
        unique_together = ('position', 'trip')

    def __str__(self):
        return smart_text(f"w{self.position}")

class Discount(models.Model):
    sku = models.CharField(max_length = 128)
    title = models.CharField(max_length = 128)
    deadline = models.DateField()
    available = models.BooleanField(default = True)
    precentage = models.PositiveIntegerField()

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def save(self, *args, **kwargs):
        self.sku = secrets.token_urlsafe(15)
        super(Discount, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.title)

class Trip(models.Model):
    GENDERS = (
        ('m', _('مرد')),
        ('f', _('خانم')),
        ('d', _('مختلط'))
    )

    CAPACITIES = (
        (1, _('تک سرنشین')),
        (2, _('دو سرنشین')),
        (3, _('سه سرنشین')),
        (4, _('چهار سرنشین')),
    )

    CREATOR_TYPES = (
        (1, _('راننده')),
        (2, _('مسافر'))
    )

    STATES = (
        (1, _('صحیح')),
        (2, _('لغو')),
    )

    ENDINGS = (
        (1, _('در حال اجرا')),
        (2, _('تمام شده'))
    )

    DISCOUNTS = (
        ('15', _('15%')),
        ('25', _('25%')),
        ('50', _('50%')),
    )

    start_time = models.DateTimeField(verbose_name=_('start time'))
    origin = models.ForeignKey(City, on_delete = models.CASCADE, related_name = 'trip_origin', verbose_name=_('origin'))
    destination = models.ForeignKey(City, on_delete = models.CASCADE, related_name = 'trip_dest', verbose_name=_('destination'))
    origin_region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name = 'trip_reg_origin', verbose_name=_('origin region'))
    destination_region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name='trip_reg_dest', verbose_name=_('destination region'))
    type_creator = models.PositiveSmallIntegerField(choices = CREATOR_TYPES, verbose_name = _('creator type'))
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name='trip', verbose_name=_('driver'))
    discount = models.CharField(choices = DISCOUNTS, max_length = 2, null = True, verbose_name = _("discount"))
    is_dispatcher = models.BooleanField(default = False)
    item_capacity = models.PositiveIntegerField(verbose_name = _('Item Capacity'), null = True)
    status = models.PositiveSmallIntegerField(choices = ENDINGS, verbose_name=_('status'))
    gender = models.CharField(max_length = 1, choices = GENDERS, default = 'd', verbose_name=_('gender'))
    front_seat_price = models.PositiveIntegerField(verbose_name = _('front_seat_price'), null = True)
    back_seat_price = models.PositiveIntegerField(verbose_name = _('back_seat_price'), null = True)
    passenger_capacity = models.PositiveSmallIntegerField(choices = CAPACITIES, null = True, verbose_name = _('passenger_capacity'))
    active = models.BooleanField(default = True, verbose_name=_('active'))
    state = models.PositiveSmallIntegerField(default = 1, choices = STATES, verbose_name= _('state'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = TripModelManager()

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')
        ordering = ('status', '-start_time',)

    
    def __str__(self):
        return "{} is {} and {}".format(self.driver, self.active, self.state)
    
