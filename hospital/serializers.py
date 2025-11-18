# hospital/serializers.py
from rest_framework import serializers
from .models import Patient, Doctor, Appointment

# Serializer for Patient model
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

# Serializer for Doctor model
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

# Serializer for Appointment model
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    # Prevent double booking for doctors
    def validate(self, data):
        doctor = data['doctor']
        date = data['appointment_date']
        if Appointment.objects.filter(doctor=doctor, appointment_date=date).exists():
            raise serializers.ValidationError("Doctor is already booked at this time.")
        return data
