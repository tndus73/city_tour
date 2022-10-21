from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('board/', views.board),
    path('board/<int:pk>/', views.posting, name="posting"),
    path('board/writing/', views.writing),
    path('board/<int:post_id>/remove/', views.remove, name="remove"),
]