from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import generic
from comentarios.forms import ComentariosCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = "comentarios/comentarios.html"

class ComentariosCreateView(LoginRequiredMixin, CreateView):
    model = Comentarios
    template_name = "comentarios/createcomentario.html"
    form_class = ComentariosCreateForm
    success_url = reverse_lazy('posts:listposts')

class ComentariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentarios
    template_name = "comentarios/updatecomentarios.html"
    fields = ['comentarios']
    success_url = reverse_lazy('posts:listposts')

class ComentariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = "comentarios/deletecomentario.html"
    success_url = reverse_lazy('posts:listposts')

