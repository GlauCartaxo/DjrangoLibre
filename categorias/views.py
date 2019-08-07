from django.shortcuts import render
from categorias.models import Categorias
from django.views.generic import ListView, CreateView
from django.views import generic
from categorias.forms import CategoriasCreateForm
# Create your views here.


class CategoriasListView(ListView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = 'categorias/categorias.html'


class CategoriasCreateView(CreateView):
    model = Categorias
    template_name = "categorias/categorias.html"
    form_class = CategoriasCreateForm
