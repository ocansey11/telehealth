from django.contrib import admin
from .models import MedicalRecord, Diagnosis

admin.site.register(MedicalRecord)
admin.site.register(Diagnosis)
