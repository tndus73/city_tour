from django.shortcuts import render
from django.shortcuts import redirect
from .models import Board
# Create your views here.

def board(request):
    #모든 Board가져와 저장
    lists = Board.objects.all()
    return render(request, 'board.html', {'lists': lists})

def posting(request, pk):
    #pk로 한개 게시글 검색
    post = Board.objects.get(id=pk)
    return render(request, 'posting.html', {'post': post})

def writing(request):
    if request.method == 'POST':
            new_article = Board.objects.create(
                name=request.POST['name'],
                contents=request.POST['contents'],
            )
            return redirect('/board/board/')
    return render(request, 'writing.html')