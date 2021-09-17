from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "posts/about.html")


def blog_single(request):
    return render(request, "posts/blog-single.html")


def categories(request):
    return render(request, "posts/categories.html")


def contact(request):
    return render(request, "posts/contact.html")