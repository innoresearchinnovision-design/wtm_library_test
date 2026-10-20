from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UserProfile
# Create your views here.

def userprofile_view(request):
    User=get_user_model()
    user = request.user
    get_user_profile = User.objects.get(id=user.id)
    context = {
        "user_profile":get_user_profile
    }

    return render(request,"auth/userprofile.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home:index")
        else:
            messages.error(request,"Invalid username or password. Please tryagain.!")
    else:
        login_form = LoginForm()

    context={
        'login':login_form
    }
    return render(request,"auth/login.html",context)

def registration_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            create_user=registration_form.save()
            create_user.save()
            UserProfile.objects.create(user=create_user)
            messages.success(request,"Successfully created acccount, Try Logging In")
            return redirect("accounts:login")
    else:
        registration_form = RegistrationForm()

    grace = {
        "register":registration_form
    }
    return render(request,"auth/registration.html",grace)

def logout_view(request):
    logout(request)
    return redirect("accounts:login")