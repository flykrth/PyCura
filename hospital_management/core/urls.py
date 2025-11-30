from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('dashboard/admin/', views.dashboard_admin, name="dashboard_admin"),
    path('dashboard/doctor/', views.dashboard_doctor, name="dashboard_doctor"),
    path('dashboard/patient/', views.dashboard_patient, name="dashboard_patient"),

    path('patients/', views.patients, name="patients"),
    path('patients/create/', views.create_patient, name="create_patient"),

    path('doctors/', views.doctors, name="doctors"),
    path('doctors/create/', views.create_doctor, name="create_doctor"),

    path('rooms/', views.rooms, name="rooms"),
    path('rooms/create/', views.create_room, name="create_room"),

    path('medicines/', views.medicines, name="medicines"),
    path('medicines/create/', views.create_medicine, name="create_medicine"),

    path('appointments/', views.appointments, name="appointments"),
    path('appointments/create/', views.create_appointment, name="create_appointment"),

    path('billing/', views.billings, name="billings"),
    path('billing/create/', views.create_billing, name="create_billing"),
]
