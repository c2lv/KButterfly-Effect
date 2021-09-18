from django.shortcuts import render

# Create your views here.

def blog_single(request):
    return render(request, "posts/blog-single.html")


def categories(request):
    return render(request, "posts/categories.html")

