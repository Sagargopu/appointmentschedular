from django.forms import ModelForm
from .models import *
from Professor.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student

class OfficeHoursForm(ModelForm):
    class Meta:
        model=OfficeHours
        fields='__all__'
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['First_Name','Last_Name','Department_id','Phone','Address','City','State','Email','Zipcode']
        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Department_id': forms.Select(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'State': forms.TextInput(attrs={'class': 'form-control'}),
            'Zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

