from django.db import models

from accounts.models import User

from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from .submodels.detail import Feature
from .submodels.detail import Bank
from .submodels.detail import Machine
from .submodels.detail import Favorites
from .submodels.detail import Notifications
from .submodels.detail import Setting

class GeneralProfile(models.Model):
    GENDERS = (
        ('m', _('male')),
        ('f', _('female')),
    )

    DEGREES = (
        (1, _('diploma')),
        (2, _('associate')),
        (3, _('bachelor')),
        (4, _('master')),
        (5, _('phd')),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile', verbose_name = _('User'))

    # required
    gender = models.CharField(max_length = 1, choices = GENDERS, default='m', null = True, blank = True, verbose_name = _('gender'))
    birth_date = models.DateField(null = True, blank = True, verbose_name = _('birth_date'))
    national_code = models.CharField(max_length = 10, null = True, blank = True, verbose_name = _('national_code'))
    tel = models.CharField(max_length=20, null = True, blank = True, verbose_name = _('tel'))
    mobile = models.CharField(max_length=11, null = True, blank = True, verbose_name = _('mobile'))
    adr = models.CharField(max_length = 256, null = True, blank = True, verbose_name = _('adr'))
    postal_code = models.CharField(max_length = 10, null = True, blank = True, verbose_name = _('postal_code'))
    credit = models.IntegerField(default = 0, verbose_name= _('credit'))

    pic = models.ImageField(upload_to = 'profile/user/', null = True, blank = True, verbose_name = _('pic'))
    national_code_pic = models.ImageField(upload_to = 'profile/user/', null = True, blank = True, verbose_name = _('national_code_pic'))

    # not required
    edu_degree = models.PositiveSmallIntegerField( choices = DEGREES, null = True, blank = True, verbose_name = _('edu_degree'))
    about = models.TextField(null = True, blank = True, verbose_name = _('about'))

class Driver(models.Model):
    job = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('job'))
    job_place = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('job_place'))
    emergency_number = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('emergency_number'))
    score = models.PositiveIntegerField(default = 0, verbose_name = _('score'))
    profile = models.OneToOneField(GeneralProfile, on_delete = models.CASCADE, related_name='driver', verbose_name = _('profile'))

    def __str__(self):
        return f'({self.profile.user.id}) {self.profile.user.first_name} {self.profile.user.last_name}'

class Passenger(models.Model):
    job = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('job'))
    emergency_number = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('emergency_number'))
    score = models.PositiveIntegerField(default = 0, verbose_name = _('score'))
    profile = models.OneToOneField(GeneralProfile, on_delete = models.CASCADE, related_name='passenger', verbose_name = _('profile'))

    def __str__(self):
        return f'({self.profile.user.id}) {self.profile.user.first_name} {self.profile.user.last_name}'
    
class Transmit(models.Model):
    job = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('job'))
    emergency_number = models.CharField(max_length = 128, null = True, blank = True, verbose_name = _('emergency_number'))
    score = models.PositiveIntegerField(default = 0, verbose_name = _('score'))
    profile = models.OneToOneField(GeneralProfile, on_delete = models.CASCADE, related_name='transmit', verbose_name = _('profile'))
    
    def __str__(self):
        return f'({self.profile.user.id}) {self.profile.user.first_name} {self.profile.user.last_name}'

