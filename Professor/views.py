from datetime import timezone
import datetime
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomRegistrationForm
from .models import Department,Professor,OfficeHours,Appointment
from Student.models import Student
from datetime import date
from datetime import datetime
from .forms import *
from Student.forms import StudentForm
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required(login_url='login')
def departments(request):
    superuser=request.user.is_superuser
    context={'departments':departments,'superuser':superuser}
    return render(request,'departments.html',context)

@login_required(login_url='login')
def Professors(request):
    Professors=Professor.objects.all()
    context={'Professors':Professors}
    return render(request,'professors.html',context)

@login_required(login_url='login')
def MySchedule(request):
    professor=Professor.objects.get(user=request.user)
    current_date = date.today()
    current_time = datetime.now()
    appointments=Appointment.objects.filter(Professor=professor,Date__gte=current_date).exclude(Date=current_date, Time__lt=current_time)
    context={'appointments':appointments}
    return render(request,'professors/myschedule.html',context)

@login_required(login_url='login')
def MyAppointments(request):
    user = request.user
    if Student.objects.filter(user=user).exists():
            student=Student.objects.get(user=request.user)
            appointments=Appointment.objects.filter(Student=student)
            context={'appointments':appointments}
            for rec in appointments:
                print(rec.Professor)
            return render(request,'professors/myappointments.html',context)
    else:
            is_professor = True
            professor=Professor.objects.get(user=request.user)
            current_date = date.today()
            current_time = datetime.now()
            appointments=Appointment.objects.filter(Professor=professor,Date__gte=current_date,Confirmed=True).exclude(Date=current_date, Time__lt=current_time)
            context={'appointments':appointments}
            return render(request,'professors/myappointments.html',context)

@login_required(login_url='login')
def Refresh(request):
    professor = Professor.objects.get(user=request.user)
    Hours = OfficeHours.objects.filter(Professor=professor)
    changes=0
    emptyAppointments=Appointment.objects.filter(Professor=professor,Confirmed=False)
    for emptyAppointment in emptyAppointments:
        emptyAppointment.delete()
    for hour in Hours:
        slots = hour.generate_time_slots()
        day = hour.Day
        date = hour.next_occurrence_of_weekday(day)
        print(date)
        for slot in slots:
                if not Appointment.objects.filter(Professor=professor, Date=date, Day=day,Time=slot).exists():
                    appointment = Appointment.objects.create(
                        Professor=professor,
                        Date=date,
                        Day=day,
                        Time=slot,
                        Student=None,
                        Confirmed=False
                    )

                    appointment.save()
                    changes+=1       
                        
    messages.success(request, 'Schedule Published Successfully!')
    return redirect('myschedule')




#login User
def LoginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('professors')
    if request.method=="POST":
        username=request.POST['Username']
        password=request.POST['Password']
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!')
            return render(request,'login.html')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            user = request.user
            if Student.objects.filter(user=user).exists():
                messages.success(request, 'You have been logged in successfully!')
                return redirect('professors')
            else:
                messages.success(request, 'You have been logged in successfully!')
                return redirect('officehours')
            
        else:
            messages.error(request, 'Username and Password does not match')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

# logout user
@login_required(login_url='login')
def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')
    
#New user registration
def SignUp(request): 
    if request.user.is_authenticated:
        return redirect('professors')
    form=CustomRegistrationForm()
    if request.method=='POST':
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save( commit=False)
            user.username=user.username.lower()
            user.save()
            user_role = form.cleaned_data['user_role']
            if user_role == 'student':
                Student.objects.create(
                    user=user,
                    First_Name=form.cleaned_data['first_name'],
                    Last_Name=form.cleaned_data['last_name'],
                    Email=form.cleaned_data['email']
                )
            if user_role == 'professor':
                Professor.objects.create(
                    user=user,
                    First_Name=form.cleaned_data['first_name'],
                    Last_Name=form.cleaned_data['last_name'],
                    Email=form.cleaned_data['email']
                )
            messages.success(request, 'User was created successfully! Update Your Profile')
            login(request,user)
            return redirect('professors')
        else:
            messages.error(request, 'Error! User already exists or Passwords does not match!')
    page='register'
    context={'page':page,'form':form}
    return render(request,'login.html',context)

@login_required(login_url='login')
def updateProfile(request):
    profile = request.user
    if Student.objects.filter(user=profile).exists():
        student = Student.objects.get(user=profile)
        form = StudentForm(instance=student)
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('profile')
    else:
        professor = Professor.objects.get(user=profile)
        form = ProfessorForm(instance=professor)
        if request.method == 'POST':
            form = ProfessorForm(request.POST, instance=professor)
            if form.is_valid():
                form.save()
                return redirect('profile') 

    context = {'form': form}
    return render(request, 'updateprofile.html', context)


@login_required(login_url='login')
def ViewOfficeHours(request):
    professor=Professor.objects.get(user=request.user)
    officehours=OfficeHours.objects.filter(Professor=professor)
    office=professor.Office
    for rec in officehours:
        print(rec.id)
    context={'officehours':officehours,'office':office}
    return render(request,'professors/officehours.html',context)

@login_required(login_url='login')
def AddOfficeHours(request):
    professor=Professor.objects.get(user=request.user)
    if request.method == 'POST':
        form = OfficeHoursForm(request.POST)
        if form.is_valid():
            office_hours = form.save(commit=False)
            office_hours.Professor=professor
            office_hours.Office=professor
            if OfficeHours.objects.filter(Professor=professor,Day=office_hours.Day).exists():
                StartTime1=OfficeHours.objects.filter(Professor=professor,Day=office_hours.Day).first().StartTime
                EndTime1=OfficeHours.objects.filter(Professor=professor,Day=office_hours.Day).first().EndTime
                StartTime2=office_hours.StartTime
                EndTime2=office_hours.EndTime
                if EndTime1 <= StartTime2 or EndTime2 <= StartTime1:
                    office_hours.save()
                    return redirect('officehours')
                else:
                    messages.error(request,'These hours are overlapping with existing office hours!')
                    return redirect('officehours')
            else:
                office_hours.save()
                return redirect('addappointments')
    else:
        form = OfficeHoursForm()
    return render(request, 'professors/addofficehours.html', {'form': form})

@login_required(login_url='login')
def DeleteOfficeHours(request,id):
    officehours=OfficeHours.objects.get(id=id)
    officehours.delete()
    return redirect('addappointments')
