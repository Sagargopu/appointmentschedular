from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User
from Student.models import Department,Student
from datetime import datetime, timedelta
from django.utils import timezone
# Create your models here.
class Professor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Department_id=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=False) 
    Office=models.CharField(max_length=1000,null=True,blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural='Professors'
        ordering=['Last_Name']
    def __str__(self):
        return f'{self.Last_Name}, {self.First_Name}'

class OfficeHours(models.Model):
    DAY_CHOICES = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    )
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,blank=False,null=False,editable=False)
    Professor=models.ForeignKey(Professor,blank=True,null=True,on_delete=models.SET_NULL)
    Day=models.CharField(max_length=3, choices=DAY_CHOICES)
    StartTime=models.TimeField()
    EndTime=models.TimeField()
    Office = models.ForeignKey('Professor', related_name='office_hours', blank=True, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural="Office Hours"
        ordering = ['Professor','Day']
    def __str__(self):
        return f"{self.Professor}, {self.Day}"
    def generate_time_slots(self):
        start_time = datetime.combine(datetime.today(), self.StartTime)
        end_time = datetime.combine(datetime.today(), self.EndTime)
        interval = timedelta(minutes=15)
        time_slots = []
        while start_time < end_time:
            time_slots.append(start_time.time())
            start_time += interval
        return time_slots
    
    def next_occurrence_of_weekday(cls, target_day_short):
        weekdays_short = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        target_day_index = weekdays_short.index(target_day_short.title()[:3])
        current_date = timezone.now()
        current_weekday = current_date.weekday()

        if target_day_index >= current_weekday:
            days_ahead = target_day_index - current_weekday
        else:
            days_ahead = 7 - current_weekday + target_day_index

        next_date = current_date + timedelta(days=days_ahead)
        return next_date.strftime("%Y-%m-%d")
    
class Appointment(models.Model):
    AppointmentId=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,blank=False,null=False,editable=False)
    Professor=models.ForeignKey(Professor,blank=True,null=True,on_delete=models.CASCADE)
    Date=models.DateField()
    Day=models.CharField(max_length=10,null=True)
    Time=models.TimeField()
    Student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.SET_NULL)
    Confirmed=models.BooleanField()
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural="Appointments"
        ordering = ['Date','Time','Professor','Day']
    def __str__(self):
        return f"{self.Professor} on {self.Date},{self.Day} at {self.Time}"
    

