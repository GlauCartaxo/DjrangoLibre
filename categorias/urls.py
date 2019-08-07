from DjangoLibre.urls import path
from categorias.views import CategoriasListView, CategoriasCreateView
from categorias.forms import CategoriasCreateForm

app_name = 'categorias'

urlpatterns = [
    path('categorias', CategoriasListView.as_view(), name='categorias'),
    path('addcategorias', CategoriasCreateView.as_view, name = 'addcategorias')
]
