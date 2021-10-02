from django.shortcuts import render
from posts.models import Post

# Create your views here.
def index(request):
    a = list(Post.objects.all().order_by("?"))
    b = a[0]
    c = a[2]
    context = {
        "b":b,
        "c":c,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def mainpage(request):
    return render(request, "main/mainpage.html")