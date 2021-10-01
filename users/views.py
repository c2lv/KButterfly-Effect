from django.shortcuts import render,redirect
from .models import Todolist
# Create your views here.
from django.utils import timezone
from django.utils.timezone import timedelta
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def mypage(request):
    user=request.user
    mylist=Todolist.objects.filter(writer=user)
    start={}
    dead={}
    for i in mylist:
        start[i.id]=i.date_start.replace(microsecond=0).isoformat()[:-3]
        dead[i.id]=i.date_deadline.replace(microsecond=0).isoformat()[:-3]
        print(start[i.id])
    return render(request,"users/mypage.html",{"lists":mylist,"starts":start,"deads":dead})

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
    return redirect("users:mypage")

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
    return redirect("users:mypage")

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
    
# def delete(request, id): # delete
#     delete_post = Post.objects.get(id=id)
#     delete_post.delete()
#     return redirect("posts:postlist")