from django.urls import path
from . import views

app_name = 'board'

board = views.Board

urlpatterns = [
    path('<str:cate>/', views.index, name='board_index'),
    path('<str:cate>/<int:board_pk>/edit', views.update, name='board_update'),
    path('<str:cate>/create/', views.create, name='board_create'),
    path('<str:cate>/<int:board_pk>/', views.detail, name='board_detail'),
]
