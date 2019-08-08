from posts.models import Posts
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import generic
from posts.forms import PostsCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PostsListView(ListView):
    model = Posts 
    context_object_name = 'posts'
    template_name = 'posts\listPosts.html'
    ordering = ['-created_at',]

class PostAddCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = "posts/addposts.html"
    form_class = PostsCreateForm
    success_url = reverse_lazy('posts:listposts')


class PostsUpdateView(LoginRequiredMixin, UpdateView):
    model = Posts
    template_name = "posts/edit.html"
    fields = ['author', 'conteudo']
    success_url = reverse_lazy('posts:listposts')


class PostsDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    context_object_name = 'posts'
    template_name = "posts/delete.html"
    success_url = reverse_lazy('posts:listposts')

