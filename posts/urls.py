from django.urls import path
from .views import *


app_name = 'posts'
urlpatterns = [
   
    path("blog_single/",blog_single, name="blog_single"),
    path("postlist/",postlist, name="postlist"),
    path('new_post/',new_post,name="new_post"),
    path('create/',create,name="create"),
    path('detail/<int:id>',detail,name="detail"),
    path('edit_post/<int:id>',edit_post,name="edit_post"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
]