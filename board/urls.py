from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('board/', views.board, name="board"),
    path('board/<int:pk>/', views.posting, name="posting"),
    path('board/writing/', views.writing, name="writing"),
    path('board/<int:post_id>/remove/', views.remove, name="remove"),
    path('board/<int:post_id>/update/', views.update, name="update"),
]