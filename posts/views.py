from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}

    return render(request, 'posts/detail.html', context)


@login_required
def new(request):

    return render(request, 'posts/new.html')


@login_required
def create(request):

    user = request.user
    body = request.POST['body']
    post = Post(user=user, body=body, created_at=timezone.now())
    post.save()

    return redirect('posts:detail', post_id=post.id)


@login_required
def edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    context = {'post': post}
    return render(request, 'posts/edit.html', context)


@login_required
def update(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    post.body = request.POST['body']
    post.save()

    return redirect('posts:detail', post_id=post.id)


@login_required
def delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    post.delete()

    return redirect('posts:index')
