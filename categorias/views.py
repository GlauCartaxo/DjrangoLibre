from django.shortcuts import render
from categorias.models import Categorias
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views import generic
from categorias.forms import CategoriasCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class CategoriasCreateView(LoginRequiredMixin, CreateView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = "categorias/addcategorias.html"
    form_class = CategoriasCreateForm
    success_url = reverse_lazy('posts:addposts')

class CategoriasUpdateView(LoginRequiredMixin, UpdateView):
    model = Categorias
    context_object_name = 'editcategorias'
    template_name = 'categorias/editcategorias.html'
    fields = ['nome']
    success_url = reverse_lazy('posts:listposts')


class CategoriasDeleteView(LoginRequiredMixin, DeleteView):
    model = Categorias
    context_object_name = 'delcategorias'
    template_name = "categorias/delcategorias.html"
    success_url = reverse_lazy('posts:listposts')
