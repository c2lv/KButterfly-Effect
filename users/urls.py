from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("mypage", mypage, name="mypage"),
    path("makelist",makelist,name="makelist"),
    path("deletelist",deletelist,name="deletelist"),
    path("updatelist/<int:id>",updatelist,name="updatelist"),
    path("addlist/<int:post_id>",addlist,name="addlist"),
    path("todolist/<int:arrange>",todolist,name="todolist"),
    path("introduce/", introduce, name="introduce"),
    path("<int:id>/posts", user_posts, name="user_posts"),
    path("edit/", edit, name="edit"),
    path("update/", update, name="update"),
    path("fin/<int:id>",fin,name="fin"),
]