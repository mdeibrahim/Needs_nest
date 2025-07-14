# urls.py
from django.urls import path
# from rest_framework_simplejwt.views import (TokenObtainPairView)
from .views import LogoutAPIView, RegisterAPIView, ForgetPasswordAPIView, ResetPasswordAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),   # JWT Login
    path('forgot-password/', ForgetPasswordAPIView.as_view(), name='forgot_password'),
    path('reset-password/<uid>/<token>/', ResetPasswordAPIView.as_view(), name='reset_password'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
