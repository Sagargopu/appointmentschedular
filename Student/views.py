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

