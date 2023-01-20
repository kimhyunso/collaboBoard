from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Category, Comment
from .forms import BoardForm, CategoryForm, CommentForm
from django.views.decorators.http import require_http_methods, require_safe


class Board:
    @require_safe
    def index(request):
        # 카테고리에 있는 내용을 가지고 온다....
        context = {
            'board' : BoardForm(),
            'categorys' : CategoryForm(),
        }
        return render(request, 'board/index.html', context)

    @require_safe
    def detail(request, board_pk):
        board = BoardForm(pk=board_pk)
        comment = CommentForm() 
        context = {
            'board' : board,
            'comment' : comment,
        }
        return render(request, 'board/detail.html', context)

    @require_http_methods(['POST', 'GET'])
    def update(request, board_pk):
        board = get_object_or_404(Board, board_pk)
        if request.method == 'POST':
            pass
        else:
            pass
        return redirect('board:board_detail', board.pk)
    
    @require_http_methods(['POST', 'GET'])
    def create(request):
        if request.method == 'POST':
            pass
        else:
            pass
        return redirect('board:board_detail', )

    
    @require_http_methods(['POST'])
    def delete(request, board_pk):
        return redirect('board:board_index')
