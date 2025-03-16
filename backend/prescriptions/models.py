from django.db import models
from doctors.models import DoctorProfile
from medical_records.models import MedicalRecord
from medications.models import Medication
from pharmacy.models import Pharmacy  # if already built

class Prescription(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='prescriptions')
    prescribed_by = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription for {self.medical_record.patient} on {self.date.date()}"

class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medications')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    
    dosage = models.CharField(max_length=100)       # e.g., "1 tablet"
    frequency = models.CharField(max_length=100)    # e.g., "2x daily"
    duration = models.CharField(max_length=100)     # e.g., "5 days"

    def __str__(self):
        return f"{self.medication.name} for {self.prescription}"
