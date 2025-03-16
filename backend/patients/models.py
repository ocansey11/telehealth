import uuid
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]


    # Unique Patient ID using UUID
    patient_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # Optional
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Handling country code and phone number separately
    country_code = models.CharField(max_length=5, default="+233")  # Default Ghana
    phone_number = models.CharField(max_length=15, unique=True)  # Stores '0504971397'
    
    email = models.EmailField(unique=True, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)  # Added nationality
    
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=100, blank=True, null=True)

    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_country_code = models.CharField(max_length=5, default="+233")  # Emergency number country code
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_phone_number(self):
        """Return the complete phone number as stored in the database."""
        return f"{self.country_code}{self.phone_number}"

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()
