from django.db import models

# Create your models here.


class Hashtag(models.Model):
    name = models.CharField(max_length=256)


class Post(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    content = models.TextField(max_length=10000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
