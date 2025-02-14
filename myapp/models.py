from django.db import models

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    full_name = models.CharField(max_length=255)
    location_description = models.CharField(max_length=255)
    mrn = models.CharField(max_length=50)
    appointment_description = models.TextField()
    appointment_comment = models.TextField(null=True, blank=True)
    appointment_type = models.CharField(max_length=100)
    customize_date = models.CharField(max_length=100)
    default_division = models.CharField(max_length=100)
    location_region = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    main_appt = models.CharField(max_length=10)
    phressia_filter = models.CharField(max_length=10)
    provider_type_group = models.CharField(max_length=100)
    quality_specialty = models.CharField(max_length=100)
    walk_in_filter = models.CharField(max_length=50)
    appt_scheduled_by = models.CharField(max_length=100)
    provider_type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.full_name} - {self.date}"
