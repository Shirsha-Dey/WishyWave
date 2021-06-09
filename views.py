from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from diagnosticcentre.models import Contact
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index(request):
    return render(request, 'index.html')
   #  return HttpResponse("Diagnostic Centre")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("services page")


def gallery(request): 
    return render(request, 'gallery.html')
    # return HttpResponse("gallery page")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        contactus = Contact(name=name, email=email, phone=phone, service=service, message=message, date= datetime.today())
        contactus.save()

    return render(request, 'contactus.html')
    # return HttpResponse("contactus page")

def admin(request): 
    return render(request, 'admin.html')
    # return HttpResponse("admin page")

def doctor(request): 
    return render(request, 'doctor.html')
    # return HttpResponse("doctor page")

def indexx(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'indexx.html')

def Login(request):
    error=""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"
        except:
            error="yes"
    d = {'error':error}                
    return render(request, 'login.html', d)
    #return HttpResponse("This is login page")


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html', d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n = request.POST['name']
        t = request.POST['title']
        g = request.POST['gender']
        d = request.POST['dob']
        q = request.POST['qualification']
        l = request.POST['license']
        c = request.POST['centerid']
        a = request.POST['address']
        p = request.POST['phone']
        e = request.POST['email']
        try:
            Doctor.objects.create(name=n,title=t,gender=g,dob=d,qualification=q,license=l,centerid=c,address=a,phone=p,email=e)
            error="no"
        except:
            error="yes"
    d = {'error':error}                
    return render(request, 'add_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        r1 = request.POST['registration1']
        r2 = request.POST['registration2']
        n = request.POST['name']
        g = request.POST['gender']
        d1 = request.POST['dob']
        a = request.POST['address']
        p = request.POST['phone']
        h = request.POST['hospital']
        t1 = request.POST['testdate']
        t2 = request.POST['testtype']
        d2 = request.POST['doctorname']
        f = request.POST['fees']
        try:
            Patient.objects.create(registration1=r1,registration2=r2,name=n,gender=g,dob=d1,address=a,phone=p,hospital=h,testdate=t1,testtype=t2,doctorname=d2,fees=f)
            error="no"
        except:
            error="yes"
    d = {'error':error}                
    return render(request, 'add_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html', d)
    #return HttpResponse("This is login page")

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()    
    if request.method=="POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date1']
        t1 = request.POST['time1']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}                
    return render(request, 'add_appointment.html', d)
    #return HttpResponse("This is login page")

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')    




def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
