from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    Department_id=models.UUIDField(default=uuid.uuid4,primary_key=True,blank=False,null=False,editable=False)
    Department_Code=models.CharField(max_length=5)
    Department_Name=models.CharField(max_length=100)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural="Departments"
        ordering=['Department_Code']
    def __str__(self):
        return self.Department_Name
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Department_id=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=False) 
    Zipcode=models.CharField(max_length=100,null=True,blank=True)  
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True) 
    class Meta:
        verbose_name_plural='Students'
        ordering=['Last_Name']
    def __str__(self):
        return f'{self.Last_Name}, {self.First_Name}'