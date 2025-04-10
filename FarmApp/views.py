from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import requests
# Create your views here.

def home_view(request):
    return render(request,'home.html')

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
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_view(request):
    # Fetch weather data from an API
    city="Jalandhar"
    weatherstack_api_key = "27631a69e40d2738bf2c838450a37ae8"
    weatherstack_url = f"http://api.weatherstack.com/current?access_key={weatherstack_api_key}&query={city}"

    try:
        response = requests.get(weatherstack_url)
        weather_data = response.json()

        if response.status_code == 200 and "current" in weather_data:
            weather = {
                "temperature": weather_data["current"]["temperature"],
                "humidity": weather_data["current"]["humidity"],
                "rain_chance": weather_data["current"].get("precip", 0)
            }
        else:
            weather = {"temperature": "N/A", "humidity": "N/A", "rain_chance": "N/A"}
            messages.error(request, "Failed to fetch weather data.")
    except Exception as e:
        weather = {"temperature": "N/A", "humidity": "N/A", "rain_chance": "N/A"}
        messages.error(request, "Error fetching weather data.")

    context = {
        "weather": weather,
        "soil": {"moisture": 42, "ph": 6.8, "nutrients": "NPK Balanced"},
        "crops": {"active": 5, "yield": 2300},
        "tasks": [
            "Irrigate corn field",
            "Fertilize tomato plants",
            "Inspect greenhouse sensors"
        ],
        "inventory": {"seeds": "100kg", "fertilizers": "25kg", "tools": 12},
        "alerts": ["Low water level in Zone B", "Pest alert in tomato section"],
        "team": {"online": 3, "completed": 7}
    }
    return render(request, 'dashboard.html', context)