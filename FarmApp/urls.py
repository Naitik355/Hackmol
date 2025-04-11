from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view,name='home'),
    path('login/', views.login_view,name='login'),
    path('signup/', views.signup_view,name='signup'),
    path('pesticides/',views.pesticides_view,name='pesticides'),
    path('about/', views.about_view, name='about'),
    path('logout/', views.logout_view,name='logout'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('profile/', views.profile_view,name='profile'),
    path('predict/', views.crop_prediction_view,name='predict'),
    path('/crop_prediction', views.crop_prediction_view,name='predict'),
    path('products/', views.products_view,name='products'),
]