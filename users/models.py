from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0) # 퍼온거 한횟수
    personal_eco_point= models.IntegerField(default=0) #개인 에코점수

class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    name=models.CharField(max_length=40) # 할 일 이름
    description=models.TextField() #  할 일 설명
    date_start= models.DateTimeField(auto_now=False) # 시작일
    date_deadline=models.DateTimeField(auto_now=False) # 마감일
    pub_date = models.DateTimeField(auto_now=True) # 생성일, 사용은 X
    p_or_o = models.BooleanField(default=False) # 개인이 만든건지 공식적인건지 False는 개인 True는 공식 
    
