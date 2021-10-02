from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# Create your views here.

def blog_single(request):
    return render(request, "posts/blog-single.html")
# @login_required 로그인 필요하면 사용하기 

def postlist(request): # post 목록
    posts= Post.objects.all()

    hashtag_dict={}

    for i in posts:
        # print(i.hashtag)
        jd=json.decoder.JSONDecoder()
        hashtag_list=jd.decode(i.hashtag)
        hashtag_dict[i.id]=hashtag_list
    
    # print(hashtag_dict)
    return render(request, "posts/postlist.html",{"posts":posts,"hashtag":hashtag_dict})

def new_post(request): # post 입력페이지
    return render(request, "posts/new_post.html")

def create(request): # create
    new_post = Post()
    new_post.title = request.POST["title"]
    new_post.title_tag = request.POST["title_tag"]
    hashtag=request.POST["hashtag"].split()
    new_post.hashtag = json.dumps(hashtag)
    
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.deadline = request.POST['deadline']
    new_post.body = request.POST["body"]
    new_post.image = request.FILES.get("image")
    new_post.save()
    return redirect("posts:detail", new_post.id)

def detail(request, id): # post 세부페이지
    post = get_object_or_404(Post, pk=id)

    hashtag_dict={}
    jd=json.decoder.JSONDecoder()
    hashtag_list=jd.decode(post.hashtag)

    return render(request, "posts/detail.html", {"post": post,"hashtag":hashtag_list})

def edit_post(request, id): # post 수정페이지
    edit_post = Post.objects.get(id=id)

    hashtag_dict={}
    jd=json.decoder.JSONDecoder()
    hashtag=jd.decode(edit_post.hashtag)

    return render(request, "posts/edit_post.html", {"post": edit_post,"hashtag":hashtag})

def update(request, id): # update
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.title_tag = request.POST["title_tag"]
    hashtag=request.POST["hashtag"].split()
    update_post.hashtag = json.dumps(hashtag)
    
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

@require_POST
@login_required
def like_toggle(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post_like,post_like_created=Like.objects.get_or_create(user=request.user,post=post)

    if not post_like_created:
        post_like.delete()
        result="like_cancel"

    else:
        result="like"

    context={
        "like_count":post.like_count,
        "result":result
    }

    return HttpResponse(json.dumps(context),content_type="application/json")


