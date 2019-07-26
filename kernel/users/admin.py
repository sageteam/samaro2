from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from django.urls import reverse
from django.utils.safestring import mark_safe

from .actions import make_active
from .actions import make_deactive

from .models import User
from .models import GeneralProfile
from .models import Driver
from .models import Passenger
from .models import Transmit

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = GeneralProfile
    can_delete = False
    verbose_name_plural = 'General Profile'
    fk_name = 'user'
    
    
    fieldsets = [
        ('I. Personal Information', {
            'fields': ['national_code', 'tel', 'mobile', 'adr'],
            'classes': ['collapse']
        }),
        ('II. Personal Information', {
            'fields':[ 'gender', 'birth_date', 'edu_degree', 'about'],
            'classes': ['collapse']
        }),
        ('III. Personal Information', {
            'fields': [ 'national_code_pic', 'pic', 'postal_code'],
            'classes': ['collapse']
        })
    ]   


class PassengerInline(admin.StackedInline):
    model = Passenger
    can_delete = False
    verbose_name_plural = 'Passenger Profile'
    fk_name = 'profile'
    fieldsets = [
        ('I. Personal Information', {
                'fields':['job', 'emergency_number'],
                'classes': ['collapse']
        })
    ]


class TransmitInline(admin.StackedInline):
    model = Transmit
    can_delete = False
    verbose_name_plural = 'Transmit Profile'
    fk_name = 'profile'
    fieldsets = [
        ('I. Personal Information', {
                'fields':['job', 'emergency_number'],
                'classes': ['collapse']
        })
    ]


class DriverInline(admin.StackedInline):
    model = Driver
    can_delete = False
    verbose_name_plural = 'Driver Profile'
    fk_name = 'profile'
    fieldsets = [
        ('I. Personal Information', {
                'fields':['job', 'emergency_number', 'job_place'],
                'classes': ['collapse']
        }),
        ('II. Personal Information', {
            'fields': ['car_name', 'car_color', 'car_model', 'car_date', 'car_chassis', 'plaque'],
            'classes': ['collapse']
        }),
        ('III. Personal Information', {
            'fields': ['driver_card', 'machine_card', 'car_pic', 'misdiagnosis'],
            'classes': ['collapse']
        }),
        ('IV. Personal Information', {
            'fields': ['passenger', 'goods'],
            'classes': ['collapse']
        }),
        ('V. Personal Information', {
            'fields': ['bank_acc_name', 'bank_name', 'bank_sheba', 'bank_card'],
            'classes': ['collapse']
        })
    ]

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


    list_display = ('email', 'first_name', 'last_name', 'is_active', 'phone_number')
    # inlines = (ProfileInline, )

    search_fields = ('email', 'phone_number', 'last_name')
    # list_filter = ('profile__role', 'is_active', 'is_staff')

    inlines = (
        ProfileInline,
    )
    

    actions = [make_active, make_deactive]
    ordering = ('email',)

admin.site.site_header = "Samaro"
admin.site.site_title = "Samaro"
admin.site.index_title = "Welcome to Samaro portal"