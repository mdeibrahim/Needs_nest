# from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, ForgetPasswordSerializer, ResetPasswordSerializer

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User registered successfully.",
                "status_code": "201",
                "id": serializer.instance.id,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserRegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserRegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User profile updated successfully.",
                "status_code": "200",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ForgetPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response({
                "message": "Password reset email sent successfully.",
                "status_code": "200"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordAPIView(APIView):
    def post(self, request, uid, token):
        try:
            # Decode the user ID
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            return Response({
                "error": "Invalid user ID.",
                "status_code": "400"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if token is valid
        if not default_token_generator.check_token(user, token):
            return Response({
                "error": "Invalid or expired token.",
                "status_code": "400"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Validate and save new password
        data = request.data.copy()
        data['uid'] = uid
        data['token'] = token
        
        serializer = ResetPasswordSerializer(data=data)
        if serializer.is_valid():
            # Set the new password
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            
            return Response({
                "message": "Password reset successfully.",
                "status_code": "200"
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)