from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User,Profile

class Userregistration(UserCreationForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Your Name",'class': 'form-control form-control-lg'}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Your username",'class': 'form-control form-control-lg'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Enter Your email",'class': 'form-control form-control-lg'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Your Phone Number",'class': 'form-control form-control-lg'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Your password",'class': 'form-control form-control-lg'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repeat Your Password",'class': 'form-control form-control-lg'}))
    class Meta:
        model=User
        fields=["full_name","username","email",'phone',"password1","password2"]
        