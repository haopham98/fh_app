from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from .models import UserProfile


# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users or create a new user.
    """
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_user(request):
    """
    Create a new user.
    """
    if request.method == 'GET':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
    if request.method == 'PUT':
        try:
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                user = UserProfile.objects.get(pk=pk)
                serializer.update(user, serializer.validated_data)
                print(serializer.validated_data)

                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
    
    return Response({'error': 'Method not allowed'}, status=405)
