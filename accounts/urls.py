from django.urls import path
from django.contrib.auth.views import LoginView
from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration')
    ]