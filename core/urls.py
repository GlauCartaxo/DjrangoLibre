from DjangoLibre.urls import path 

from core.views import index

app_name ='core'

urlpatterns = [
    path('home', index, name='index'), #pagian inicial, view, name
]