from django.shortcuts import HttpResponse,get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from user.models import User

# Create your views here.

def index(request):
    if request.method == 'GET':
        context = dict()
        context['users'] = User.objects.all()
        context['posts'] = Post.objects.all().order_by('-created_at')
        return render(request, 'post/post/index.html', context=context)
    
@login_required(login_url='user:signin')
def post_detail(request, post_id):
    if request.method == 'GET':
        context = dict()
        context['post'] = Post.objects.get(id=post_id)
        context['comment'] = Comment.objects.filter(post_id=post_id).order_by('-created_at')
        return render(request, 'post/post/post_detail.html', context=context)
    
@login_required(login_url='user:signin')
def my_list(request, user_id):
    if request.method == 'GET':
        context = dict()
        context['user'] = User.objects.get(id=user_id)
        context['posts'] = Post.objects.filter(id=user_id)
        return render(request, 'post/post/post_mylist.html', context=context)

# 게시글 생성, 수정, 삭제
def create(request):
    if request.method == 'GET':
        context = dict()
        context['users'] = User.objects.all()
        context['posts'] = Post.objects.all()
        return render(request,'post/post/post_create.html', context=context)
    elif request.method =='POST':
        post = Post()
        post.title = request.POST.get('title')
        post.image = request.FILES.get('image')
        post.content = request.POST.get('content')
        post.author = request.user
        post.save()
        return redirect('post:post-detail',post_id=post.id)

def update(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post,id=post_id)
        context={'post':post}
        return render(request,'post/post/post_update.html',context)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.image = request.FILES.get('image')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:index')


def delete(request, post_id):
    pass


# comment
@login_required(login_url='user:signin')
def comment_create(request, comment_id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id=comment_id)
        content = request.POST.get('content')
        Comment.objects.create(content=content, author=user, post=post)
        return redirect('post:post-detail', post.id)

@login_required(login_url='user:signin')
def comment_update(request, comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment,id=comment_id)
        context={'comment':comment}
        return render(request, 'post/post/comment_update_form.html', context=context)
    elif request.method == 'POST':
        update_comment = Comment.objects.get(id=comment_id)
        post_id = update_comment.post.id
        update_comment.content = request.POST.get('content')
        update_comment.save()
        return redirect('/post/detail/'+str(post_id))

@login_required(login_url='user:signin')
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    current_post = comment.post.id
    comment.delete()
    return redirect('post:post-detail', current_post)