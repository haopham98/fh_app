from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer
from .models import Food
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response as Respone
from django.core.paginator import Paginator

# Create your views here.


@api_view(['GET'])
def food_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()

        paginator = Paginator(foods, 5)  # 5 food mỗi trang
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'food_list.html', {
            'page_obj': page_obj,
            'foods': foods
        })
    
def food_create(request):
    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Respone(serializer.data, status=201)
        return Respone(serializer.errors, status=400)
    
    return Respone({"detail": "Method not allowed"}, status=405)