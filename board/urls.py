from django.urls import path
from . import views

app_name = 'board'

board = views.Board

urlpatterns = [
    path('', board.index, name='board_index'),
    path('<str:category>/', board.index, name='board_main'),
    path('<str:category>/<int:board_pk>/edit', board.update, name='board_update'),
    path('<str:category>/create/', board.create, name='board_create'),
    path('<str:category>/<int:board_pk>/', board.detail, name='board_detail'),
]
