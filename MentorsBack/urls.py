from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import RegisterAPIView, AuthAPIView, UserViewSet

router = routers.DefaultRouter()
router.register('list', UserViewSet) # 유저리스트 (테스트용)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", RegisterAPIView.as_view()),  # post - 회원가입
    path("api/user/auth/", AuthAPIView.as_view()),  # post - 로그인, delete - 로그아웃, get - 유저정보
    path("api/user/auth/refresh/", TokenRefreshView.as_view()),  # jwt 토큰 재발급
    path("", include(router.urls)),
]
