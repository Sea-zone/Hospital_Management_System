# hospital/admin.py
from django.contrib import admin
from .models import Patient, Doctor, Appointment

# Register models to appear in Django admin
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone')
    search_fields = ('name', 'specialization', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment_date')
    list_filter = ('doctor', 'appointment_date')
    search_fields = ('patient__name', 'doctor__name')
