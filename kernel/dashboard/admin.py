from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from khayyam import JalaliDatetime as jd

from .models import FAQ
from .models import FAQCategory
from .models import Rules
from .models import RulesCategory
# from .models import Setting

# Register your models here.
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    '''Admin View for FAQ'''

    list_display = ('title', 'category', 'activate', 'Created', 'Modified', 'Show_Category')
    list_filter = ('activate', 'category', 'modified', 'created')
    field = ('title', 'activate', 'category')    
    readonly_fields = ('created', 'modified')
    search_fields = ('title', 'description')
    ordering = ('created', 'activate')

    def Show_Category(self, obj):
        display_text = ", ".join([
            "<a href={} target=\"_blank\">ویرایش دسته بندی</a>".format(
                reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name),
                        args=(obj.pk,)))
        ])
        if obj.pk:
            return mark_safe(display_text)
        return "-"

    def Created(self, obj):
        p_date = jd(obj.created).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.created).strftime('%Q')
        return e_date
    
    def Modified(self, obj):
        p_date = jd(obj.modified).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.modified).strftime('%Q')
        return e_date

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)


@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    '''Admin View for FAQCategory'''

    list_display = ('title', 'created', 'modified')
    list_filter = ('created', 'modified')
    readonly_fields = ('created', 'modified', 'sku')
    search_fields = ('title',)
    ordering = ('-created',)
    # raw_id_fields =('faq',)


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_model_perms(self, request):
        return {}


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    '''Admin View for Rules'''

    list_display = ('title', 'category', 'activate', 'Created', 'Modified', 'Show_Category')
    list_filter = ('activate', 'category', 'modified', 'created')
    field = ('title', 'activate', 'category')    
    readonly_fields = ('created', 'modified')
    search_fields = ('title', 'description')
    ordering = ('created', 'activate')

    def Show_Category(self, obj):
        display_text = ", ".join([
            "<a href={} target=\"_blank\">ویرایش دسته بندی</a>".format(
                reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name),
                        args=(obj.pk,)))
        ])
        if obj.pk:
            return mark_safe(display_text)
        return "-"

    def Created(self, obj):
        p_date = jd(obj.created).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.created).strftime('%Q')
        return e_date
    
    def Modified(self, obj):
        p_date = jd(obj.modified).strftime('%C')
        display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
        # return mark_safe(display_text)

        e_date = date_point = jd(obj.modified).strftime('%Q')
        return e_date

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)


@admin.register(RulesCategory)
class RulesCategoryAdmin(admin.ModelAdmin):
    '''Admin View for RulesCategory'''

    list_display = ('title', 'created', 'modified')
    list_filter = ('created', 'modified')
    readonly_fields = ('created', 'modified', 'sku')
    search_fields = ('title',)
    ordering = ('-created',)


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_model_perms(self, request):
        return {}


# @admin.register(Setting)
# class SettingAdmin(admin.ModelAdmin):
#     '''Admin View for Setting'''

#     list_display = ('get_message_from', 'subscribe', 'email_transaction', 'email_trip_info', 'Modified')
#     list_filter = ('get_message_from', 'subscribe', 'email_transaction', 'email_trip_info')
#     ordering = ('-modified',)

#     def Modified(self, obj):
#         p_date = jd(obj.modified).strftime('%C')
#         display_text = f'<p style="font-family: \'samim\';">{p_date}</p>'
#         # return mark_safe(display_text)

#         e_date = date_point = jd(obj.modified).strftime('%Q')
#         return e_date
