from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from Professor.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def Students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'students/students.html',context)

@login_required(login_url='login')
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
    
@login_required(login_url='login')
def ViewAppointments(request,pk):
    user=User.objects.get(username=pk)
    professor=Professor.objects.get(user=user)
    appointments=Appointment.objects.filter(Professor=professor)
    context={'appointments':appointments,'professor':professor}
    return render(request,'students/viewappointments.html',context)

@login_required(login_url='login')
def BookAppointment(request,pk):
    student=Student.objects.get(user=request.user)
    appointment=Appointment.objects.get(AppointmentId=pk)
    if Appointment.objects.filter(Student=student,Date=appointment.Date,Time=appointment.Time).exists():
        messages.error(request, 'You already have an appointment for this selected time!')
    else:
        appointment.Student=student
        appointment.Confirmed=True
        appointment.save()
        Subject='Appointment Confirmation'
        Body=f"Your appointment has been scheduled!\n\nThis is to confirm your upcoming appointment with {appointment.Professor.First_Name} {appointment.Professor.Last_Name} scheduled for {appointment.Date} at {appointment.Time} at {appointment.Professor.Office}. Please ensure you are present on time. If you need to reschedule, kindly check my schedule and reschedule the appointment at your earliest convenience.\n\nBest regards,\n{appointment.Professor.First_Name} {appointment.Professor.Last_Name}."
        send_mail(
            Subject, Body, settings.EMAIL_HOST_USER, [student.Email], fail_silently=False
        )
    return redirect('myappointments')

@login_required(login_url='login')
def CancelAppointment(request,pk):
    appointment=Appointment.objects.get(AppointmentId=pk)
    student=appointment.Student
    appointment.Student=None
    appointment.Confirmed=False
    appointment.save()
    Subject='Appointment Cancelled'
    Body=f"Your appointment has been cancelled!\n\nThis is to confirm you have cancelled upcoming appointment with {appointment.Professor.First_Name} {appointment.Professor.Last_Name} on {appointment.Date} at {appointment.Time} at {appointment.Professor.Office}. If you need to reschedule, kindly check my schedule and reschedule the appointment at your convenience.\n\nBest regards,\n{appointment.Professor.First_Name} {appointment.Professor.Last_Name}."
    send_mail(
            Subject, Body, settings.EMAIL_HOST_USER, [student.Email], fail_silently=False
        )
    return redirect('myappointments')