from django.urls import path
from . import views


urlpatterns = [
    path('page/<int:page_id>/<slug:page_slug>/', views.page_view, name="page"),
]
