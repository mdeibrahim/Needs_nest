# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView)
from .views import RegisterAPIView, ForgetPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # JWT Login
    path('forgot-password/', ForgetPasswordAPIView.as_view(), name='forgot_password'),
    path('reset-password/<uid>/<token>/', ResetPasswordAPIView.as_view(), name='reset_password'),
    
]
