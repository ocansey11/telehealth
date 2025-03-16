from django.db import models
from patients.models import Patient
import uuid

class MedicalHistory(models.Model):
    """
    One-time health background provided by the patient (onboarding).
    """
    history_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name="medical_history")

    blood_group = models.CharField(max_length=20, choices=[
        ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('UNKNOWN', 'Unknown')
    ], default="UNKNOWN")

    genotype = models.CharField(max_length=10, choices=[
        ('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('SC', 'SC'), ('CC', 'CC'), ('UNKNOWN', 'Unknown')
    ], default="UNKNOWN")

    height_cm = models.FloatField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)

    chronic_conditions = models.ManyToManyField("ChronicCondition", blank=True)
    past_surgeries = models.ManyToManyField("SurgicalHistory", blank=True)
    allergies = models.ManyToManyField("Allergy", blank=True)

    hospitalizations = models.TextField(blank=True, null=True)
    implants = models.TextField(blank=True, null=True)

    smoking_status = models.BooleanField(default=False)
    alcohol_consumption = models.CharField(max_length=50, choices=[
        ('None', 'None'), ('Occasional', 'Occasional'), ('Regular', 'Regular')
    ], default='None')

    diet_and_exercise = models.TextField(blank=True, null=True)

    prostate_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')
    cervical_cancer_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')
    breast_cancer_screening = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='N/A')

    last_vital_signs = models.TextField(blank=True, null=True)
    recent_lab_results = models.ImageField(upload_to="lab_results/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_bmi(self):
        if self.height_cm and self.weight_kg:
            height_m = self.height_cm / 100
            return round(self.weight_kg / (height_m ** 2), 2)
        return None

    def __str__(self):
        return f"Medical History for {self.patient}"
