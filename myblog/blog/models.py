from turtle import title
from django.db import models

class Post(models.Model):
    Title = models.CharField(max lenght=200)
    text = models.CharField()
    created_date = models.DateTimeField
class author(models.Model):
    Post = models.ForeignKey(Post,on_delete = models.CASCADE)
    published_date = models.DateTimeField

