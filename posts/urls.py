from django.urls import path
from . import views as blogs_views


urlpatterns = [
    path('blog/', blogs_views.blog , name="blog"),
    path('blog/<int:category_id>/', blogs_views.category , name="category_blog"),
]
