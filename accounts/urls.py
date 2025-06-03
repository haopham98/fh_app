from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),  # Include user profile URLs
    path('register/', views.register)
]