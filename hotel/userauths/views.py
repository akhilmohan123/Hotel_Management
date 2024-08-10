from django.shortcuts import render,redirect
from . forms import Userregistration
from django.contrib.auth import authenticate, login
from . models import Profile,User
from django.contrib import messages
def Registrationview(request):
    if request.user.is_authenticated:
        print("hello")
        messages.warning(request,f"You are already logged in")
        return redirect("index")
    form=Userregistration(request.POST or None)
    if form.is_valid():
        form.save()
        full_name=form.cleaned_data.get("full_name")
        phone=form.cleaned_data.get("phone")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        user=authenticate(email=email,password=password)
        login(user)
        messages.success(request,f"hey {full_name}")
        profile=Profile.objects.get(user=request.user)
        profile.full_name=full_name
        profile.phone=phone
        profile.save()
        return redirect("index")

    context={
        "form":form
    }
    return render(request,"userauth/signup.html",context)
