from django.db import models
from prescriptions.models import Prescription
from patients.models import Patient
from pharmacy.models import Pharmacy

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled'),
    ]

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='deliveries')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='deliveries')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    delivery_address = models.TextField()
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)

    return_reason = models.TextField(blank=True, null=True)
    returned_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery for {self.patient} - {self.status}"
