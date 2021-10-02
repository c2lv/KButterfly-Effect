from django.shortcuts import render
from django.contrib.auth.models import User

from users.models import Profile
# Create your views here.
def index(request):
    top=Profile.objects.all().order_by('-personal_eco_point')
    
    top4=top[:4]
    
    return render(request, "index.html",{"top4":top4})

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def mainpage(request):
    return render(request, "main/mainpage.html")