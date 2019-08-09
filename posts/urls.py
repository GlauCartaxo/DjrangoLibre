from DjangoLibre.urls import path

from posts.views import PostsListView, PostAddCreateView, PostsUpdateView, PostsDeleteView, PostsDetailView

app_name ='posts'

urlpatterns = [
    path('posts', PostsListView.as_view(), name='listposts' ),
    path('addposts', PostAddCreateView.as_view(), name='addposts'),
    path('posts/<int:pk>/alterar', PostsUpdateView.as_view(), name = 'updateposts'),
    path('posts/<int:pk>/apagar', PostsDeleteView.as_view(), name = 'deleteposts'),
    path('posts/<int:pk>/detail', PostsDetailView.as_view(), name='detailposts'),

]