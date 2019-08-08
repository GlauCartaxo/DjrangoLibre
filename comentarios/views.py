from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import generic
from comentarios.forms import ComentariosCreateForm
from django.urls import reverse_lazy

# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = "comentarios/comentarios.html"

class ComentariosCreateView(CreateView):
    model = Comentarios
    template_name = "comentarios/createcomentario.html"
    form_class = ComentariosCreateForm
    success_url = reverse_lazy('posts:listposts')

class ComentariosUpdateView(UpdateView):
    model = Comentarios
    template_name = "comentarios/updatecomentarios.html"
    fields = ['comentarios']
    success_url = reverse_lazy('posts:listposts')

class ComentariosDeleteView(DeleteView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = "comentarios/deletecomentario.html"
    success_url = reverse_lazy('posts:listposts')

