from . import views
from django.urls import path, include

urlpatterns = [
    path('list/', views.food_list, name='food-list'),
]