from django.contrib import admin
from django.urls import path
from diagnosticcentre import views

urlpatterns = [
    path("", views.indexx, name='indexx'),
    path("index", views.index, name='home'),
    path("services", views.services, name='services'),
    path("gallery", views.gallery, name='gallery'),
    path("contactus", views.contactus, name='contactus'),
    path("admin", views.admin, name='admin'),
    path("doctor", views.doctor, name='doctor'),
    path("admin_login/", views.Login, name='login'),
    path("logout/", views.Logout_admin, name='logout'),
    path("view_doctor/", views.View_Doctor, name='view_doctor'),
    path("add_doctor/", views.Add_Doctor, name='add_doctor'),
    path("delete_doctor(?P<int:pid>)", views.Delete_Doctor, name='delete_doctor'),
    path("view_patient/", views.View_Patient, name='view_patient'),
    path("add_patient/", views.Add_Patient, name='add_patient'),
    path("delete_patient(?P<int:pid>)", views.Delete_Patient, name='delete_patient'),
    path("view_appointment/", views.View_Appointment, name='view_appointment'),
    path("add_appointment/", views.Add_Appointment, name='add_appointment'),
    path("delete_appointment(?P<int:pid>)", views.Delete_Appointment, name='delete_appointment'),


]
