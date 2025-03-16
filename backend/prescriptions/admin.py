from django.contrib import admin
from .models import Prescription, PrescriptionMedication

admin.site.register(Prescription)
admin.site.register(PrescriptionMedication)
