from django import forms
from posts.models import Posts

class PostsCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['author', 'conteudo', 'categorias', ]
   