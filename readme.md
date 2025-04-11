# Farm Dashboard

A comprehensive web application for modern farming management, providing real-time monitoring, crop prediction, and farm management tools.

## Overview

Farm Dashboard is a Django-based web application designed to help farmers and agricultural professionals manage their farming operations efficiently. The application provides features for weather monitoring, crop prediction, farm inventory management, and task tracking.

## Features

- **User Authentication**: Secure login and registration system
- **Weather Monitoring**: Real-time weather data integration
- **Crop Prediction**: Machine learning-based crop recommendation system
- **Farm Management**: 
  - Soil condition monitoring
  - Crop tracking
  - Task management
  - Inventory tracking
- **Profile Management**: User profile customization
- **Dashboard**: Comprehensive overview of farm operations

## Tech Stack

- **Backend**: 
  - Django (Python web framework)
  - SQLite database
  - Joblib for machine learning model handling
- **Frontend**:
  - HTML/CSS
  - JavaScript
- **APIs**:
  - Weatherstack API for weather data
- **Machine Learning**:
  - Scikit-learn (for crop prediction model)

## Prerequisites

- Python 3.x
- Django
- Joblib
- Requests library
- Weatherstack API key

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Naitik355/Hackmol
   cd FarmDashboard
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add:
   ```
   WEATHERSTACK_API_KEY=your_api_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
FarmDashboard/
├── FarmApp/
│   ├── models/           # Machine learning models
│   ├── templates/        # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # URL routing
│   └── admin.py         # Admin configuration
├── manage.py            # Django management script
└── db.sqlite3           # Database file
```

## Usage

1. **Registration**: Create a new account using the signup page
2. **Login**: Access your dashboard using your credentials
3. **Dashboard**: View farm statistics, weather data, and manage tasks
4. **Crop Prediction**: Input soil and weather parameters to get crop recommendations
5. **Profile Management**: Update your personal information and preferences

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weatherstack API for weather data
- Django community for the excellent web framework
- Scikit-learn for machine learning capabilities