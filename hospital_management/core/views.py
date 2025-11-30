from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def login_user(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            role = user.profile.role
            if role == "admin":
                return redirect("dashboard_admin")
            elif role == "doctor":
                return redirect("dashboard_doctor")
            else:
                return redirect("dashboard_patient")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_admin(request):
    return render(request, "dashboard_admin.html")

@login_required
def dashboard_doctor(request):
    return render(request, "dashboard_doctor.html")

@login_required
def dashboard_patient(request):
    return render(request, "dashboard_patient.html")


# -------- PATIENT CRUD --------
def patients(request):
    return render(request, "patients.html", {"patients": Patient.objects.all()})


def create_patient(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['name']
        )
        Profile.objects.create(user=user, role="patient")
        Patient.objects.create(user=user, age=request.POST['age'], address=request.POST['address'])
        return redirect("patients")

    return render(request, "create_patient.html")


# -------- DOCTOR CRUD --------
def doctors(request):
    return render(request, "doctors.html", {"doctors": Doctor.objects.all()})


def create_doctor(request):
    if request.method == "POST":
        u = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['name']
        )
        Profile.objects.create(user=u, role="doctor")
        Doctor.objects.create(user=u, specialization=request.POST['specialization'])
        return redirect("doctors")
    return render(request, "create_doctor.html")


# -------- ROOMS --------
def rooms(request):
    return render(request, "rooms.html", {"rooms": Room.objects.all()})


def create_room(request):
    if request.method == "POST":
        Room.objects.create(
            number=request.POST['number'],
            type=request.POST['type'],
            is_available=True
        )
        return redirect("rooms")
    return render(request, "create_room.html")


# -------- MEDICINES --------
def medicines(request):
    return render(request, "medicines.html", {"med": Medicine.objects.all()})


def create_medicine(request):
    if request.method == "POST":
        Medicine.objects.create(name=request.POST['name'], quantity=request.POST['quantity'])
        return redirect("medicines")
    return render(request, "create_medicine.html")


# -------- APPOINTMENTS --------
def appointments(request):
    return render(request, "appointments.html", {
        "appointments": Appointment.objects.all()
    })


def create_appointment(request):
    if request.method == "POST":
        Appointment.objects.create(
            patient=Patient.objects.get(id=request.POST['patient']),
            doctor=Doctor.objects.get(id=request.POST['doctor']),
            date=request.POST['date'],
            description=request.POST['description']
        )
        return redirect("appointments")

    return render(request, "create_appointment.html", {
        "patients": Patient.objects.all(),
        "doctors": Doctor.objects.all()
    })


# -------- BILLINGS --------
def billings(request):
    return render(request, "billings.html", {"bills": Billing.objects.all()})


def create_billing(request):
    if request.method == "POST":
        total = int(request.POST['doctor_fee']) + int(request.POST['room_fee']) + int(request.POST['medicine_fee'])
        Billing.objects.create(
            patient=Patient.objects.get(id=request.POST['patient']),
            doctor_fee=request.POST['doctor_fee'],
            room_fee=request.POST['room_fee'],
            medicine_fee=request.POST['medicine_fee'],
            total=total
        )
        return redirect("billings")

    return render(request, "create_billing.html", {
        "patients": Patient.objects.all()
    })
