from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import RegisterAPIView, AuthAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("auth/", AuthAPIView.as_view()), # post - 로그인, delete - 로그아웃, get - 유저정보
    path("auth/refresh/", TokenRefreshView.as_view()), # jwt 토큰 재발급

]