from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import requests
import joblib
import os
import warnings
from django.conf import settings
import joblib

# Create your views here.

def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def pesticides_view(request):
    return render(request,'pesticides.html')

def products_view(request):
    return render(request,'products.html')

def profile_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')

        user = User.objects.get(username=request.user.username)
        user.username = username
        user.email = email
        user.phone = phone
        user.city = city
        user.state = state
        user.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('dashboard')
    
    return render(request, 'profile.html')

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
    weatherstack_api_key = "82a694a694ec993d6c20080dff911346"
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
        messages.error(request, f"Error fetching weather data: {e}")

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

def crop_prediction_view(request):
    if request.method == 'POST':
        try:
            nitrogen = float(request.POST.get('N'))
            phosphorus = float(request.POST.get('P'))
            potassium = float(request.POST.get('K'))
            temperature = float(request.POST.get('temperature'))
            humidity = float(request.POST.get('humidity'))
            ph = float(request.POST.get('ph'))
            rainfall = float(request.POST.get('rainfall'))

            model_path = os.path.join(settings.BASE_DIR, 'FarmApp', 'models', 'crop_model.pkl')
            model = joblib.load(model_path)
            print("Received values:", nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                prediction = model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
                crop_name = prediction[0]

            return render(request, 'dashboard.html', {'crop_name': crop_name})

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, 'dashboard.html')    

    return render(request, 'home.html')