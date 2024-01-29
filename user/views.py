from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    user_type = data.get('user_type')

    if not username or not password or not email or not user_type:
        return Response({'error': 'Please provide all required fields'})

    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'User with this email already exists'})

    
    if user_type not in [choice[0] for choice in User.USER_TYPE_CHOICES]:
        return Response({'error': 'Invalid user type'})

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        user_type=user_type
    )

    group, created = Group.objects.get_or_create(name=user_type)
    user.groups.add(group)

    return Response({'message': 'User registered successfully'})

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        print(f"User {user.username} authenticated successfully.")
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        print(f"Authentication failed for email: {email}")
        return Response({'error': 'Invalid credentials'})
    
@api_view(['POST'])  
@ permission_classes([IsAdminUser])  
def owner_create(request):
    email = request.data.get('email')
    password = request.data.get('password')
    group = Group.objects.get(name = 'Owner')
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        hash_password = make_password(password)
        a = User.objects.create(email = email, password = hash_password)
        a.groups.add(group)
        return Response('User created.')
    else:
        return Response(serializer.errors)    


    

@api_view(["GET"])

def grouplist(request):
    group_objs = Group.objects.all().exclude(name = 'Owner')
    serializer = GroupSerializer(group_objs, many = True)
    return Response (serializer.data)
    