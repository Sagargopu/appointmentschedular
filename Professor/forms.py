from django.forms import ModelForm
from .models import *
from Professor.models import *
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class OfficeHoursForm(forms.ModelForm):
    class Meta:
        model = OfficeHours
        fields = ['Professor','Day', 'StartTime', 'EndTime', 'Office']
        widgets = {
            'Professor': forms.HiddenInput(),
            'Day': forms.Select(attrs={'class': 'form-control'}),
            'StartTime': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'step': '1800'}),
            'EndTime': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'step': '1800'}),
            'Office': forms.HiddenInput()
        }
class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['First_Name', 'Last_Name', 'Department_id', 'Phone', 'Email', 'Office']
        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Department_id': forms.Select(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Office': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomRegistrationForm(UserCreationForm):
    USER_ROLES = (
        ('student', 'Student'),
        ('professor', 'Professor'))
    user_role = forms.ChoiceField(choices=USER_ROLES, widget=forms.RadioSelect)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'})
        }