from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Photo(models.Model):
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']
