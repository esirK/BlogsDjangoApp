from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
         # if page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if Page is out of range, deliver last page of result
        posts = paginator.page(paginator.num_pages)

    if not page:
        page=1
    return render(request, 'blog/post/list.html', {"page": paginator.page(int(page)), "posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post/detail.html', {'post': post})
