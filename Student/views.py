from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from Professor.models import *
# Create your views here.
def Students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'students/students.html',context)

def Profile(request):
    user=User.objects.get(username=request.user)
    if Student.objects.filter(user=user).exists():
        profile=Student.objects.get(user=user)
        role='student'
        context={'profile':profile,'role':role}
        return render(request,'profile.html',context)
    else:
        profile=Professor.objects.get(user=user)
        role='professor'
        officehours=OfficeHours.objects.filter(Professor=profile)
        context={'profile':profile,'role':role,'officehours':officehours}
        return render(request,'profile.html',context)
    
def ViewAppointments(request,pk):
    user=User.objects.get(username=pk)
    professor=Professor.objects.get(user=user)
    appointments=Appointment.objects.filter(Professor=professor)
    for rec in appointments:
        print(rec)
    context={'appointments':appointments,'professor':professor}
    return render(request,'students/viewappointments.html',context)

def BookAppointment(request,pk):
    student=Student.objects.get(user=request.user)
    appointment=Appointment.objects.get(AppointmentId=pk)
    if Appointment.objects.filter(Student=student,Date=appointment.Date,Time=appointment.Time).exists():
        messages.error(request, 'You already have an appointment for this selected time!')
    else:
        appointment.Student=student
        appointment.Confirmed=True
        appointment.save()
    return redirect('myappointments')

def CancelAppointment(request,pk):
    appointment=Appointment.objects.get(AppointmentId=pk)
    print(appointment.Date)
    appointment.Student=None
    appointment.Confirmed=False
    appointment.save()
    return redirect('myappointments')