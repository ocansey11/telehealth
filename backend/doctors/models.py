from django.db import models
from users.models import User

class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=False)

    # Optional availability for calendar integration
    available_from = models.TimeField(blank=True, null=True)
    available_to = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.user.full_name}"
