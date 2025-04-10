from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# Create your views here.

def home_view(request):
    return render(request,'home.html')


def pesticides_view(request):
    return render(request,'pesticides.html')

def about_view(request):
    return render(request, 'about.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')


        if password != cpassword:
            messages.error(request, 'Passwords do not match')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            
        else:
            try:
                validate_password(password)
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                messages.success(
                    request, 'Registration successful! You can now login.')
                return redirect('login')
            
            except ValidationError as e:
                for error in e:
                    messages.error(request,error)

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        user = authenticate(request, username=username, password=password)   #gives true or false
        if user:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')