from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail)  # Include user profile URLs
]