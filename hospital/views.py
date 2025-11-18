# hospital/views.py
from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

# CRUD API for Patients
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# CRUD API for Doctors
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# CRUD API for Appointments
class AppointmentViewSet(viewsets.ModelViewSet):
    # Use select_related for database optimization
    queryset = Appointment.objects.select_related('patient', 'doctor')
    serializer_class = AppointmentSerializer
