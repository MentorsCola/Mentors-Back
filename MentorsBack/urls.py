from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from board import views
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register('list', UserViewSet) # 유저리스트 (테스트용)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin/board/", views.BoardAPI.as_view(), name="board-detail"),
    path('', include(router.urls)),
    path('', include("user.urls")),
    path('', include("board.urls")),
]
