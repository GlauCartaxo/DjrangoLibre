from django.db import models
from posts.models import Posts
# Create your models here.

class Comentarios(models.Model):
    comentarios = models.TextField()
    
    posts =models.ForeignKey("posts.Posts", verbose_name=("posts"),
    related_name= 'commentsFromPosts', on_delete=models.CASCADE)