from django.contrib import admin
from .models import DoctorProfile, Specialization

admin.site.register(Specialization)
admin.site.register(DoctorProfile)
