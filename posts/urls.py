from django.urls import path
from .views import *
from . import views

app_name = 'posts'
urlpatterns = [
    path("about/",about, name="about"),
    path("blog_single/",blog_single, name="blog_single"),
    path("categories/",categories, name="categories"),
    path("contact/",contact, name="contact"),

]