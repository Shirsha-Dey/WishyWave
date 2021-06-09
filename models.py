from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    service = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
        


class Doctor(models.Model):
    name = models.CharField(max_length=122)
    title = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    dob = models.CharField(max_length=122)
    qualification = models.CharField(max_length=122)
    license = models.CharField(max_length=122)
    centerid = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
      


    def __str__(self):
        return self.name

class Patient(models.Model):
   registration1 = models.CharField(max_length=122)
   registration2 = models.CharField(max_length=122)
   name = models.CharField(max_length=122)
   gender = models.CharField(max_length=122)
   dob = models.CharField(max_length=122)
   address = models.TextField()
   phone = models.CharField(max_length=122)
   hospital = models.CharField(max_length=122)
   testdate = models.CharField(max_length=122)
   testtype = models.CharField(max_length=122)
   doctorname = models.CharField(max_length=122)
   fees = models.CharField(max_length=122)
   
   def __str__(self):
        return self.name  

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name

    