from django.db import models

class Appointment(models.Model):
    appointment_date = models.CharField(max_length=100)
    appointment_time = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    employee_availability = models.CharField(max_length=100, blank=True, null=True)

    # Service Catalog Dropdown (Brazilian, Haircolor, Haircut)
    BRAZILIAN = 'Brazilian'
    HAIRCOLOR = 'Haircolor'
    HAIRCUT = 'Haircut'
    SERVICE_CATALOG_CHOICES = [
        (BRAZILIAN, 'Brazilian'),
        (HAIRCOLOR, 'Haircolor'),
        (HAIRCUT, 'Haircut'),
    ]
    service_catalog = models.CharField(max_length=50, choices=SERVICE_CATALOG_CHOICES, default=BRAZILIAN)

    def __str__(self):
        return f"Appointment for {self.client_name} on {self.appointment_date} at {self.appointment_time}"
