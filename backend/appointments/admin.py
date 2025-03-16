from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_datetime', 'status')
    list_filter = ('status', 'appointment_datetime')
    search_fields = ('patient__first_name', 'doctor__user__full_name')
