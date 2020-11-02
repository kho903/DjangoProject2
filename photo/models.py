# from django.contrib.auth.models import User
from member.models import User
from django.db import models


# Create your models here.


class Photo(models.Model):
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    like = models.ManyToManyField(User, blank=True, related_name='like', through='Like')

    @property
    def like_count(self):
        return self.like.count()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('member.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']


class Like(models.Model):
    user = models.ForeignKey('member.User', on_delete=models.CASCADE, related_name='like_user')
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='like_photo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
