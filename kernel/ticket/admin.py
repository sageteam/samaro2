from django.contrib import admin
from ticket.models import TicketEnvelope
from ticket.models import Department
# Register your models here.

@admin.register(TicketEnvelope)
class TicketEnvelopeAdmin(admin.ModelAdmin):
    '''Admin View for TicketEnvelope'''

    list_display = ('sku', 'subject', 'priority', 'status', 'department', 'modified')
    list_filter = ('priority', 'status', 'department')
    
    raw_id_fields = ('trip', 'driver', 'passenger')
    readonly_fields = ('sku',)
    search_fields = ('subject',)
    ordering = ('-priority', 'status', '-modified')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('-created',)