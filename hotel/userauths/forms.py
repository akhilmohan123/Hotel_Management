from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User,Profile

class Userregistration(UserCreationForm):
    full_name=forms.CharField(widget=forms.TimeInput(attrs={"placeholder":"Enter Your Name"}))
    class Meta:
        model=User
        fields=["full_name","username","email","password1","password2"]