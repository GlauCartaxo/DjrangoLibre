from DjangoLibre.urls import path
from users.views import UserListView, UserLoginView, UserLogoutView, SignupCreateView, UserDetailView

app_name ='users'

urlpatterns = [
    path('list', UserListView.as_view(), name='list_users'), #pagian inicial, view, name
    path('login', UserLoginView.as_view(), name='login_users'),
    path('logout', UserLogoutView.as_view(), name='logout_users'),
    path('signup', SignupCreateView.as_view(), name='signup_users'),
    path('users/<int:pk>/detail', UserDetailView.as_view(), name='detail_users'),
    
]