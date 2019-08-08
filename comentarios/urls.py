from DjangoLibre.urls import path

from comentarios.views import ComentariosListView, ComentariosCreateView, ComentariosUpdateView, ComentariosDeleteView
from comentarios.forms import ComentariosCreateForm

app_name ='comentarios'

urlpatterns = [
    path('comentarios', ComentariosListView.as_view(), name='listcomentarios'),
    path('addcomentarios', ComentariosCreateView.as_view(), name = 'createcomentario'),
    path('comentarios/<int:pk>/alterar', ComentariosUpdateView.as_view(), name='updatecomentarios'),
    path('comentarios/<int:pk>/deletar', ComentariosDeleteView.as_view(), name='deletecomentario'),
    
]
