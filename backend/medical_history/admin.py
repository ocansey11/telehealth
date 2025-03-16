from django.db import models
from patients.models import Patient
import uuid

class MedicalHistory(models.Model):
    history_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name="medical_history")

    # Core Medical History
    blood_group = models.CharField(max_length=20, choices=[
        ('O+', 'O+'), ('O-', 'O-'),
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('UNKNOWN', 'Unknown')
    ], default="UNKNOWN")

    genotype = models.CharField(max_length=10, choices=[
        ('AA', 'AA'), ('AS', 'AS'),
        ('SS', 'SS'), ('SC', 'SC'),
        ('CC', 'CC'), ('UNKNOWN', 'Unknown')
    ], default="UNKNOWN")

    # Physical Attributes (Measured occasionally)
    height_cm = models.FloatField(blank=True, null=True)  # Stored in cm
    weight_kg = models.FloatField(blank=True, null=True)  # Stored in kg

    # BMI Calculation
    def calculate_bmi(self):
        if self.height_cm and self.weight_kg:
            height_m = self.height_cm / 100  # Convert cm to meters
            return round(self.weight_kg / (height_m ** 2), 2)
        return None

    chronic_conditions = models.ManyToManyField("ChronicCondition", blank=True)
    past_surgeries = models.ManyToManyField("SurgicalHistory", blank=True)
    hospitalizations = models.TextField(blank=True, null=True)

    allergies = models.ManyToManyField("Allergy", blank=True)
    implants = models.TextField(blank=True, null=True)  # Pacemaker, Dental Implant, etc.

    # Lifestyle & Social History
    smoking_status = models.BooleanField(default=False)
    alcohol_consumption = models.CharField(max_length=50, choices=[
        ('None', 'None'), ('Occasional', 'Occasional'), ('Regular', 'Regular')
    ], default='None')
    diet_and_exercise = models.TextField(blank=True, null=True)

    # Screening & Preventative Health
    prostate_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')
    cervical_cancer_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')
    breast_cancer_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')

    # Last Check-Up Details
    last_vital_signs = models.TextField(blank=True, null=True)  # Deprecated, now stored in Consultation
    recent_lab_results = models.ImageField(upload_to="lab_results/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - Medical History"



class ChronicCondition(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SurgicalHistory(models.Model):
    procedure_name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.procedure_name} ({self.year})"


class Allergy(models.Model):
    name = models.CharField(max_length=255, unique=True)
    reaction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class FamilyMedicalHistory(models.Model):
    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Grandparent', 'Grandparent'),
        ('Uncle/Aunt', 'Uncle/Aunt'),
        ('Cousin', 'Cousin'),
        ('Other', 'Other'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="family_history")
    relative = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    condition = models.CharField(max_length=255)
    age_at_diagnosis = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.relative} had {self.condition}"
