from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categorias

# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey("users.User", verbose_name=("autor"), on_delete=models.CASCADE)
    categorias= models.ForeignKey("categorias.Categorias", verbose_name=("categorias"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f'Post {self.pk} | Author {self.author} | Created at {self.created_at}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'