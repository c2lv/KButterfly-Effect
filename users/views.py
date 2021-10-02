from django.shortcuts import render,redirect,get_object_or_404
from .models import Todolist
from posts.models import Post
# Create your views here.
from django.utils import timezone
from django.utils.timezone import timedelta
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta,date

def mypage(request):
    posts=Post.objects.filter(writer=request.user)
    return render(request, "users/mypage.html",{"posts":posts})

def todolist(request, arrange):
    user=request.user
    if arrange==1: # 1은 진행중
        now=datetime.today()
        mylist=Todolist.objects.filter(writer=user,date_deadline__gt=now).order_by('date_deadline')
    elif arrange==2: # 2은 오늘마감 보기
        now=datetime.today()
        today=date.today()
        tomorrow=date.today()+timedelta(days=1)
        mylist=Todolist.objects.filter(writer=user,date_deadline__gt=now,date_deadline__range=(today,tomorrow)).order_by('date_deadline')
    else: # 3은 지난거 보기
        now=datetime.today()
        mylist=Todolist.objects.filter(writer=user,date_deadline__lt=now).order_by('date_deadline')
    start={}
    dead={}
    for i in mylist:
        start[i.id]=i.date_start.replace(microsecond=0).isoformat()[:-3]
        dead[i.id]=i.date_deadline.replace(microsecond=0).isoformat()[:-3]
        # print(start[i.id])
    return render(request,"users/todolist.html",{"lists":mylist,"starts":start,"deads":dead})

def addlist(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post.shared+=1 # 포스트 공유 1 추가
    add_list=Todolist()
    add_list.name=post.title
    add_list.description=post.body+"\n 작성자 : "+str(post.writer)+"\n"+"<a href={% url 'posts:details' post.id%}>원본</a>"
    add_list.writer=request.user
    add_list.date_start=post.pub_date.replace(microsecond=0).isoformat()[:-3]
    add_list.date_deadline=post.deadline.replace(microsecond=0).isoformat()[:-3]
    add_list.pub_date=timezone.now()
    add_list.p_or_o=True
    add_list.save()
    return redirect("users:todolist",1)


def makelist(request): # 빈 투두리스트
    new_list = Todolist()
    new_list.name = ''
    new_list.description = ''
    new_list.writer = request.user
    new_list.date_start = timezone.now()
    new_list.date_deadline = timezone.now()+timedelta(hours=1)
    new_list.pub_date = timezone.now()
    # new_list.p_or_o=False #default값 있음
    new_list.save()
    return redirect("users:todolist",1)

@csrf_exempt
def updatelist(request,id): # 빈 투두리스트
    update_list = Todolist.objects.get(id=id)
    update_list.name = request.POST["name"]
    update_list.description = request.POST["description"]
    update_list.writer = request.user
    update_list.date_start = request.POST['date_start']
    update_list.date_deadline = request.POST['date_deadline']
    # print(update_list.date_start)
    update_list.pub_date = timezone.now()
    # new_list.p_or_o=False #default값 있음
    update_list.save()
    return redirect("users:todolist",1)

@csrf_exempt
def deletelist(request):
    param=json.loads(request.body)
    arr=param['checked_id']
    cnt=param['cnt']
    i=0
    
    while(i<cnt):
        deletelist=Todolist.objects.get(id=arr[i])
        deletelist.delete()
        i+=1
    if i==cnt:
        check=1
    else:
        check=0
    context={
        "check":check
    }
    
    return HttpResponse(json.dumps(context),content_type="application/json")
    