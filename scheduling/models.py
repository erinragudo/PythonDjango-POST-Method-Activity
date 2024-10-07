from django.db import models

class Appointment(models.Model):
    Appointment_Date = models.CharField(max_length=100)
    Appointment_Time = models.CharField(max_length=100)
    Client_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=15)
    # employee_availability = models.CharField(max_length=100, blank=True, null=True)

    # Service Catalog Dropdown (Brazilian, Haircolor, Haircut)
    BRAZILIAN = 'Brazilian'
    HAIRCOLOR = 'Haircolor'
    HAIRCUT = 'Haircut'
    SERVICE_CATALOG_CHOICES = [
        (BRAZILIAN, 'Brazilian'),
        (HAIRCOLOR, 'Haircolor'),
        (HAIRCUT, 'Haircut'),
    ]
    Service_Catalog = models.CharField(max_length=50, choices=SERVICE_CATALOG_CHOICES, default=BRAZILIAN)

    def __str__(self):
        return f"Appointment for {self.Client_Name} on {self.Appointment_Date} at {self.Appointment_Time}"
