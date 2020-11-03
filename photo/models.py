# from django.contrib.auth.models import User
import re

from taggit.managers import TaggableManager

from member.models import User
from django.db import models


class Photo(models.Model):
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    like = models.ManyToManyField(User, blank=True, related_name='like', through='Like')
    tags = TaggableManager(blank=True)

    # hashTag = models.ManyToManyField('Tag', blank=True)
    #
    #
    # def tag_save(self):
    #     tags = re.findall(r'#(\w+)\b', self.text)
    #
    #     if not tags:
    #         return
    #
    #     for tag in tags:
    #         tag_, tag_created = Tag.objects.get_or_create(tag_name=tag)
    #         self.hashTag.add(tag_)

    @property
    def like_count(self):
        return self.like.count()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']

#
# class Tag(models.Model):
#     tag_name = models.CharField(max_length=140, unique=True)
#
#     def __str__(self):
#         return self.tag_name


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
