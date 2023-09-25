from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = YourUserSerializer

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # Authenticate user and generate token
        # Return token and user data in response

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logout logic here
        return Response({"message": "User logged out successfully"})
