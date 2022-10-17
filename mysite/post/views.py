from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from user.models import User

# Create your views here.

@login_required(login_url='user:signin')
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
        return render(request, 'post/post/post_detail.html', context=context)
    
@login_required(login_url='user:signin')
def my_list(request, user_id):
    if request.method == 'GET':
        context = dict()
        context['user'] = User.objects.get(id=user_id)
        context['posts'] = Post.objects.filter(id=user_id)
        return render(request, 'post/post/post_mylist.html', context=context)
