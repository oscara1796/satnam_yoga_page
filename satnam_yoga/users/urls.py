from django.urls import path
from . import views as users_views


urlpatterns = [
    path('users/login/', users_views.login_view, name="login"),
    # path('users/logout/', users_views.logout, name="logout"),
    # path('users/signup/', users_views.signup, name="signup"),
]
