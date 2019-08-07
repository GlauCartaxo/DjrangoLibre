from DjangoLibre.urls import path
from categorias.views import CategoriasCreateView, CategoriasUpdateView, CategoriasDeleteView
from categorias.forms import CategoriasCreateForm

app_name = 'categorias'

urlpatterns = [
    path('addcategorias', CategoriasCreateView.as_view(), name = 'addcategorias'),
    path('categorias/<int:pk>/alterar', CategoriasUpdateView.as_view(), name = 'editcategorias'),
    path('categorias/<int:pk>/deletar', CategoriasDeleteView.as_view(), name = 'delcategorias'),
]
