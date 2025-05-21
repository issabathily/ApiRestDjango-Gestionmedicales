from django.contrib import admin

# Register your models here.
from .models import Profile, Patient, MedicalRecord, Appointment

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
