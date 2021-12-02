from django.urls import path, include
from .views import UserProfile, AdminProfile


urlpatterns = [
    path('registerUser/', UserProfile.as_view()),
    path('registerAdmin/', AdminProfile.as_view())
]