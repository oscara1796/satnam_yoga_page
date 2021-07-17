"""satnam_yoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as satnam_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('.well-known/pki-validation/E418E9768C32CF77F5A45100D28DDE3B.txt', satnam_views.serveFile, name="serveFile"),
    path('', include('store.urls')),
    path('', include('users.urls')),
    path('', include('videos.urls')),
    path('', include('payments.urls')),
    path('', include('posts.urls')),
    path('', include('contact.urls')),
    path('', include('pages.urls')),

]

urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
