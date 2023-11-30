from django.urls import path

from users.apps import UsersConfig
from users.views import signup, LoginView, user_confirm, LogoutView, users_list, activate_user, deactivate_user

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', signup, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirming/<int:pk>/', user_confirm, name='confirming'),
    path('users_list/', users_list, name='list_users'),
    path('activate_user/<int:user_id>/', activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', deactivate_user, name='deactivate_user'),
]
