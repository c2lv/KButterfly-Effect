from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
# Create your views here.

def blog_single(request):
    return render(request, "posts/blog-single.html")

# @login_required 로그인 필요하면 사용하기 

def postlist(request): # post 목록
    return render(request, "posts/postlist.html")

def new_post(request): # post 입력페이지
    return render(request, "posts/new_post.html")

def create(request): # create
    new_post = Post()
    new_post.title = request.POST["title"]
    new_post.title_tag = request.POST["title_tag"]
    new_post.hashtag = request.POST["hashtag"]
    new_post.eco_score = request.POST["eco_score"]
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.deadline = request.POST['deadline']
    new_post.body = request.POST["body"]
    new_post.image = request.FILES.get("image")
    new_post.save()
    return redirect("posts:detail", new_post.id)

def detail(request, id): # post 세부페이지
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post})

def edit_post(request, id): # post 수정페이지
    edit_post = Post.objects.get(id=id)
    return render(request, "posts/edit_post.html", {"post": edit_post})

def update(request, id): # update
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.title_tag = request.POST["title_tag"]
    update_post.hashtag = request.POST["hashtag"]
    update_post.eco_score = request.POST["eco_score"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.deadline = request.POST['deadline']
    update_post.body = request.POST["body"]
    if request.FILES.get('image'):
        update_post.image=request.FILES.get('image')
    update_post.save()
    return redirect("posts:detail", update_post.id)

def delete(request, id): # delete
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect("posts:postlist")
