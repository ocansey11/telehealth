from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage_form = models.CharField(max_length=100)  # e.g., tablet, syrup
    strength = models.CharField(max_length=50)      # e.g., 500mg

    def __str__(self):
        return f"{self.name} ({self.strength}, {self.dosage_form})"
