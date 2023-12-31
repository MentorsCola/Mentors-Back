from django.urls import path, include
from . import views

app_name = "board"

urlpatterns = [
    path("board/", views.BoardAPI.as_view(), name="board-list"),
    path("board/<int:pk>/", views.BoardDetailAPI.as_view(), name="board-detail"), # 게시물 내용 보는건 로그인을 해야함
]