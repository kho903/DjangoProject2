from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

# User : 기본 user를 상속하여 추가 field로 구성
# cf. blank=True :빈 채로 저장 & null=True : null 값으로 저장


class User(AbstractUser):

    bio = models.TextField(null=True, blank=True) # 소개
    photo = models.ImageField(upload_to='user/%Y/%m/%d', null=True, blank=True) # 프로필 사진
    phone_number = models.CharField(null= True, blank=True, max_length=20) # 전화번호
    date_of_birth = models.DateField(null=True, blank=True) # 생일
    website = models.CharField(null=True, blank=True, max_length=100) # 웹사이트


# class Member(models.Model):
#     # id, password, 닉네임, 이메일, 전화번호, 설명
#     # id, pw, nickname, email, phone_number, desc
#     name = models.CharField(max_length=20)
#     pw = models.CharField(max_length=20)
#
#     # nickname = models.CharField(max_length=20)
#     # email = models.CharField()
#     # phone_number = models.CharField(max_length=13)
#     # desc = models.TextField()
#
#     class Meta:
#         db_table = "members"
# class Post(models.Model):
#     # 닉네임, 텍스트, 이미지
#     nickname = models.CharField(max_length=20)
#     text = models.CharField(max_length=200)
#     image = models.fields #???
#     # 좋아요 수, 댓글 수
#     likes = models.IntegerField(default=0)
#     comments = models.IntegerField(default=0)
#     # 날짜
#     created = models.DateTimeField(auto_now_add=True)
#
#
# class Comments(models.Model):
#     nickname = models.CharField(max_length=20)
#     text = models.CharField(max_length=50)
#     likes = models.IntegerField(dafault=0)
