from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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

        user = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                user = UserProfile.objects.get(pk=pk)
                serializer.update(user, serializer.validated_data)
                print(serializer.validated_data)

                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            print(f"Error updating user: {e}")
            return Response({'error': 'User not found'}, status=404)
    
    if request.method == 'DELETE':
        user = get_object_or_404(UserProfile, pk=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=204)

    return Response({'error': 'Method not allowed'}, status=405)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            bio = request.data.get('bio')
            age = request.data.get('age')
            if not username or not email or not password:
                return Response(
                    {'error': 'Username, email, and password are required.'},
                    status=400
                )
            if UserProfile.objects.filter(username=username).exists():
                return Response(
                    {'error': 'Username already exists.'}, 
                    status=400
                    )
            if UserProfile.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists.'}, status=400)
            UserProfile.objects.create_user(
                username=username,
                email=email,
                password=password,
                bio=bio,
                age=age
            )
            return Response(
                {'message': 'User registered successfully.'},
                status=201
                )
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response(
            {'message': 'User registered successfully.'},
            status=201
            )

                
            