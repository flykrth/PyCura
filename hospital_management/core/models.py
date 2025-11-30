from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.first_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.user.first_name


class Room(models.Model):
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.number


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.patient} -> {self.doctor}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_fee = models.IntegerField()
    room_fee = models.IntegerField()
    medicine_fee = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"Billing for {self.patient}"
