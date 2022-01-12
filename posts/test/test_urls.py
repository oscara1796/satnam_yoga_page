from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from posts.views import *


class TestURLS(SimpleTestCase):
    """docstring forTestURLS."""


    def test_resolver_url_blog(self):
        url = reverse("blog")
        self.assertEquals(resolve(url).func, blog)


    def test_resolver_url_category(self):
        url = reverse("category_blog", args=["1"])
        self.assertEquals(resolve(url).func, category)
