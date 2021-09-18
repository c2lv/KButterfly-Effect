from django.urls import path
from .views import *


app_name = 'posts'
urlpatterns = [
   
    path("blog_single/",blog_single, name="blog_single"),
    path("categories/",categories, name="categories"),

]