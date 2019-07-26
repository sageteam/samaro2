from django.db import models

from accounts.models import User
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

class Machine(models.Model):
    # car detail
    name = models.CharField(null = True, blank = True, max_length = 128, verbose_name = _('name'))
    color = models.CharField(null = True, blank = True, max_length = 32, verbose_name = _('color'))
    model = models.CharField(null = True, blank = True, max_length = 32, verbose_name = _('model'))
    plaque = models.CharField(null = True, blank = True, max_length = 8, verbose_name = _('plaque'))
    year = models.DateField(null = True, blank = True, verbose_name = _('year'))
    chassis_number = models.CharField(null = True, blank = True, max_length = 64, verbose_name = _('chassis'))

    # uploads
    driver_card = models.ImageField(upload_to = 'profile/driver/', null = True, blank = True, verbose_name=_('driver card'))
    machine_card = models.ImageField(upload_to = 'profile/driver/', null = True, blank = True, verbose_name=_('machine card'))
    misdiagnosis = models.ImageField(upload_to = 'profile/driver/', null = True, blank = True, verbose_name=_('misdiagnosis'))
    car_pic = models.ImageField(upload_to = 'profile/driver/', null = True, blank = True, verbose_name=_('car pic'))

    features = models.ManyToManyField('Feature', related_name='machine', verbose_name = _('features'))

    driver = models.OneToOneField('Driver', on_delete = models.CASCADE, related_name='machine', verbose_name = _('driver'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Machine')
        verbose_name_plural = _('Machines')

    def __str__(self):
        return smart_text(f"{self.model}")

class Bank(models.Model):
    bank_acc_name = models.CharField(max_length = 128, null = True, blank = True, verbose_name=_('bank acc name'))
    bank_name = models.CharField(max_length = 128, null = True, blank = True, verbose_name=_('bank name'))
    bank_sheba = models.CharField(max_length = 128, null = True, blank = True, verbose_name=_('bank sheba'))
    bank_card = models.CharField(max_length = 128, null = True, blank = True, verbose_name=_('bank card'))
    driver = models.OneToOneField('Driver', on_delete = models.CASCADE, related_name='bank', verbose_name = _('driver'))

    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Banks')

    def __str__(self):
        return smart_text(f"{self.bank_acc_name}")

class Feature(models.Model):
    """Model definition for Features."""

    name = models.CharField(max_length = 128, unique = True, verbose_name = _('name'))
    status = models.BooleanField(default=False, verbose_name=_('status'))

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Features."""

        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        """Unicode representation of Features."""
        return smart_text(f'{self.name}')

class Setting(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='setting', verbose_name=_('User'))
    prefered_message = (
        ('e', _('email')),
        ('t', _('ticket')),
    )
    get_message_from = models.CharField(max_length = 1, choices = prefered_message, default = 'e', verbose_name=_('get message from'))
    subscribe = models.BooleanField(verbose_name=_('subscribe'), default = 0)
    email_transaction = models.BooleanField(verbose_name=_('email transaction'), default = 0)
    email_trip_info = models.BooleanField(verbose_name=_('email trip info'), default = 0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='favorites', verbose_name = _('User'))
    title = models.CharField(max_length = 128, verbose_name = _('title'))
    status = models.BooleanField(default = False, verbose_name = _('status'))

    class Meta:
        unique_together = ('user', 'title')

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='notifications', verbose_name=_('User'))
    point_type = (
        ('p', _('positive')),
        ('t', _('negative')),
    )
    point = models.CharField(max_length = 1, choices=point_type, verbose_name = _('point'))
    summary = models.CharField(max_length = 512, verbose_name = _('summary'))
    seen = models.BooleanField(default = False, verbose_name = _('seen'))
