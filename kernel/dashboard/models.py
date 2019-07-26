import secrets
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class FAQ(models.Model):
    """Model definition for FAQ."""

    title = models.CharField(max_length = 128, unique = True)
    description = models.TextField()
    activate = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('FAQCategory', on_delete = models.CASCADE, related_name='question')

    class Meta:
        """Meta definition for FAQ."""

        verbose_name = _('پرسش نامه')
        verbose_name_plural = _('سوالات متداول')

    def __str__(self):
        """Unicode representation of FAQ."""
        return self.title

class FAQCategory(models.Model):
    """Model definition for FAQCategory."""
    sku = models.CharField(max_length = 32, unique = True, blank = True, null = False)
    title = models.CharField(max_length = 128, unique = True)
    activate = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.sku = secrets.token_urlsafe(5)
        super(FAQCategory, self).save(*args, **kwargs)


    class Meta:
        """Meta definition for FAQCategory."""

        verbose_name = 'دسته بندی پرسش نامه'
        verbose_name_plural = 'دسته بندی سوالات'

    def __str__(self):
        """Unicode representation of FAQCategory."""
        return self.title


class Rules(models.Model):
    """Model definition for FAQ."""

    title = models.CharField(max_length = 128, unique = True)
    description = models.TextField()
    activate = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('RulesCategory', on_delete = models.CASCADE, related_name='rule')

    class Meta:
        """Meta definition for FAQ."""

        verbose_name = _('قانون')
        verbose_name_plural = _('قوانین')

    def __str__(self):
        """Unicode representation of FAQ."""
        return self.title


class RulesCategory(models.Model):
    """Model definition for FAQCategory."""
    sku = models.CharField(max_length = 32, unique = True, blank = True, null = False)
    title = models.CharField(max_length = 128, unique = True)
    activate = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.sku = secrets.token_urlsafe(5)
        super(RulesCategory, self).save(*args, **kwargs)


    class Meta:
        """Meta definition for FAQCategory."""

        verbose_name = 'دسته بندی قوانین'
        verbose_name_plural = 'دسته بندی قوانین'

    def __str__(self):
        """Unicode representation of FAQCategory."""
        return self.title

