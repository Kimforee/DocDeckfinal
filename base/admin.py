from django.contrib import admin

# Register your models here.
from .api.models import PatientData

admin.site.register(PatientData)