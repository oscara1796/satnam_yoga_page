from django.urls import path
from . import views as video_views


urlpatterns = [
    path('', video_views.list_menu , name="feed"),
]
