from django.db import models


class PatientData(models.Model):
    gender = models.CharField(max_length=1)  # Consider using choices for Male/Female
    age = models.IntegerField()
    education_years = models.IntegerField()
    socioeconomic_status = models.FloatField()
    mmse = models.FloatField()
    cdr = models.FloatField()
    etiv = models.IntegerField()
    nwbv = models.FloatField()
    asf = models.FloatField()
    predicted_category = models.CharField(max_length=50, blank=True, null=True)
