from .serializers import UserSerializer, UsersSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .models import Users

import logging

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            logging.info(refresh_token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logging.error(f"Logout error: {str(e)}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        data = request.user
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)
    
class UsersView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        data = Users.objects.all()
        serializer = UsersSerializer(data, many=True)
        return Response(serializer.data)
    
class UsersCountView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_count = Users.objects.count()
        return Response({
            'user_count': user_count
        }, status=200)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
