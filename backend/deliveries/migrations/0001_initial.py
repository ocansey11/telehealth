# Generated by Django 5.1.7 on 2025-03-16 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('pharmacy', '0001_initial'),
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('dispatched', 'Dispatched'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('delivery_address', models.TextField()),
                ('tracking_number', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('return_reason', models.TextField(blank=True, null=True)),
                ('returned_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='patients.patient')),
                ('pharmacy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.pharmacy')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='prescriptions.prescription')),
            ],
        ),
    ]
