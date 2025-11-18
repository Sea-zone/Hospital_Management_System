# hospital/models.py
from django.db import models

# Abstract base class for shared fields
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True  # This class won’t create its own table

    def __str__(self):
        return self.name

# Patient inherits from Person
class Patient(Person):
    address = models.TextField()

# Doctor inherits from Person
class Doctor(Person):
    specialization = models.CharField(max_length=100)

# Appointment model linking Patient and Doctor
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.appointment_date}"
