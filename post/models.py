from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    author_avatar = models.CharField(max_length=255)
    content = models.TextField()
    like = models.CharField(max_length=255)