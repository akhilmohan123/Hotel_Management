from django.shortcuts import render, redirect
from .forms import Userregistration
from django.contrib.auth import authenticate, login, logout
from .models import Profile,User
from django.contrib import messages
from django.db import IntegrityError

def Registrationview(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("index")
    
    form = Userregistration(request.POST or None)
    
    if form.is_valid():
        try:
            # Check if a user with the same username or email already exists
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists.')
            else:
                # Save the user using the form
                user = form.save()
                
                # Extract user details
                full_name = form.cleaned_data.get("full_name")
                phone = form.cleaned_data.get("phone")
                password = form.cleaned_data.get("password1")
                
                # Authenticate the user
                user = authenticate(request, email=email, password=password)
                print("authenticate")
                if user is not None:
                    login(request, user)
                    print("login")
                    messages.success(request, f"Hey {full_name}")
                    
                    # Create or update the user profile
                    profile, created = Profile.objects.get_or_create(user=request.user)
                    profile.full_name = full_name
                    profile.phone = phone
                    profile.save()
                    print("redirecting to index page")
                    return redirect("index")
                else:
                    print("not")
                    messages.error(request, "Authentication failed. Please check your credentials.")
        except IntegrityError as e:
            print("IntegrityError:", e)  # Log the error
            messages.error(request, "A user with this username or email already exists.")
    else:
        print("Form errors:", form.errors)  # Print form errors to debug

    context = {
        "form": form
    }
    
    return render(request, "userauth/signup.html", context)

def Logoutview(request):
    logout(request)
    return redirect("index")
