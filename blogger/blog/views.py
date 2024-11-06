from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post


def base(request: HttpRequest):
    posts = Post.objects.all().order_by('-published_at')  
    return render(request, "blog/base.html", {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published') == 'on'
        image = request.FILES.get('image')
        post = Post(title=title, content=content, is_published=is_published, image=image)
        post.save()
        return redirect('blog:base')  
    return render(request, 'blog/add_post.html')

def post_list(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/post_list.html", {'posts': posts})

def post_detail(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def update_post(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_published = request.POST.get('is_published') == 'on'
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.category = request.POST.get('category')
        post.save()
        return redirect('blog:post_detail', post_id=post.id)  

    return render(request, 'blog/update_post.html', {'post': post})

def delete_post(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('blog:base')  
   