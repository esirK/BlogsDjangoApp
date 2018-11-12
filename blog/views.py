from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
from .models import Post, Comment


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

    comments = post.comments.all()

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Form submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            import pdb; pdb.set_trace()
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})


# Class Based view
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/post/list.html'
