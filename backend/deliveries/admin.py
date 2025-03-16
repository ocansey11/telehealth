from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'pharmacy', 'status', 'delivery_date')
    list_filter = ('status', 'pharmacy')
    search_fields = ('tracking_number', 'patient__first_name', 'pharmacy__name')
