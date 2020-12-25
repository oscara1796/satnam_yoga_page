from django.urls import path
from . import views as video_views


urlpatterns = [
    path('', video_views.list_menu , name="feed"),
    path('videos', video_views.video_list , name="video_list_menu"),
    path('videos/<int:video_id>/', video_views.video_id_show , name="video_id_show"),
]
