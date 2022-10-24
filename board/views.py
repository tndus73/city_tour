from django.shortcuts import render
from django.shortcuts import redirect
from .models import Notice
from django.core.paginator import Paginator
# Create your views here.

def board(request):
    lists = Notice.objects.all() #모든 Board가져와 저장
    page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    question_list = Notice.objects.order_by('-time') # time기준으로 역순
    paginator = Paginator(question_list, 10)  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'board.html', context)

def posting(request, pk):
    #pk로 한개 게시글 검색
    post = Notice.objects.get(id=pk)
    return render(request, 'posting.html', {'post': post})

def writing(request):
    if request.method == 'POST':
            new_article = Notice.objects.create(
                title=request.POST['title'],
                name=request.POST['name'],
                contents=request.POST['contents'],
            )
            return redirect('/board/board/')
    return render(request, 'writing.html')

def remove(request, post_id):
    post = Notice.objects.get(id=post_id)
    post.delete()
    return redirect('/board/board/')

def update(request, post_id):
      post = Notice.objects.get(id=post_id)
      if request.method == "POST":
            post.title = request.POST['title']
            post.name = request.POST['name']
            post.contents = request.POST['contents']
            post.save()
            return redirect('/board/board/' + str(post.id), {'post': post})
      else:
            context = {'post':post}
            return render(request, 'update.html', context)