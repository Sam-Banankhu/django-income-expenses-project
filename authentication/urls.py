# from .views import RegistrationView
from . import views
from django.urls import path

urlpatterns = [
    path('register', views.Registration.as_view(), name='register'),
]
