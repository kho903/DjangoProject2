from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# 회원 DB

class User(AbstractUser):
    birth_date=models.DateTimeField(null=True, blank=True)
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)




# class UserManager(BaseUserManager):
#     def create_user(self, email, nickname, password=None):
#         """
#         주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
#         """
#         if not email:
#             raise ValueError(_('Users must have an email address'))
#
#         user = self.model(
#             email=self.normalize_email(email),
#             nickname=nickname,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, nickname, last_name, first_name, password):
#         """
#         주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
#         단, 최상위 사용자이므로 권한을 부여한다.
#         """
#         user = self.create_user(
#             email=email,
#             password=password,
#             nickname=nickname,
#         )
#
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(
#         verbose_name=_('Email address'),
#         max_length=255,
#         unique=True,
#     )
#     nickname = models.CharField(
#         verbose_name=_('Nickname'),
#         max_length=30,
#         unique=True
#     )
#     is_active = models.BooleanField(
#         verbose_name=_('Is active'),
#         default=True
#     )
#     date_joined = models.DateTimeField(
#         verbose_name=_('Date joined'),
#         default=timezone.now
#     )
#     # 이 필드는 레거시 시스템 호환을 위해 추가할 수도 있다.
#     salt = models.CharField(
#         verbose_name=_('Salt'),
#         max_length=10,
#         blank=True
#     )
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['nickname', ]
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#         ordering = ('-date_joined',)
#
#     def __str__(self):
#         return self.nickname
#
#     def get_full_name(self):
#         return self.nickname
#
#     def get_short_name(self):
#         return self.nickname
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All superusers are staff
#         return self.is_superuser
#
#     get_full_name.short_description = _('Full name')



#
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

#
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
