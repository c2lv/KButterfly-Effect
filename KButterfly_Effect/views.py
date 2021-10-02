from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User

from users.models import Profile
# Create your views here.
def index(request):
    a = list(Post.objects.all().order_by("?")) # 랜덤 정렬
    b = a[0]
    c = a[2]

    d = list(Post.objects.all().order_by('-like')) # 좋아요 순 정렬
    e = d[0]
    f = d[1]
    g = d[2]

    top=Profile.objects.all().order_by('-personal_eco_point')
    top4=top[:4]

    context = {
        "b":b,
        "c":c,
        "e":e,
        "f":f,
        "g":g,
        "top4":top4,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def mainpage(request):
    return render(request, "main/mainpage.html")