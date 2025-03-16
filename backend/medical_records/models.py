from django.db import models
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import DoctorProfile

class Diagnosis(models.Model):
    code = models.CharField(max_length=20, unique=True)  # e.g., ICD-10
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.description[:50]}"

class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='medical_record')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True, related_name='medical_records')

    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, blank=True)
    
    clinical_notes = models.TextField()
    vitals = models.TextField(blank=True, null=True)  # Example: "BP: 120/80, HR: 72"
    lab_requests = models.TextField(blank=True, null=True)
    follow_up_recommendation = models.TextField(blank=True, null=True)

    recorded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record for {self.patient} on {self.recorded_at.date()}"

    class Meta:
        ordering = ['-recorded_at']
