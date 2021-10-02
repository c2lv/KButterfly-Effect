from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User

from users.models import Profile
# Create your views here.
def index(request):
    a = list(Post.objects.all().order_by("?")) # 랜덤 정렬
    a2 = a[:2]

    b = list(Post.objects.all().order_by('-like')) # 좋아요 순 정렬
    b3 = b[:3]

    top=Profile.objects.all().order_by('-personal_eco_point')
    top4=top[:4]

    context = {
        "a2":a2,
        "b3":b3,
        "top4":top4,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def mainpage(request):
    return render(request, "main/mainpage.html")