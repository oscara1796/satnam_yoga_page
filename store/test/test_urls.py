from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import *

# Create your tests here.
class TestUrls(SimpleTestCase):
    """docstring forTestUrls."""



    def test_resolved_url_store(self):
        url = reverse("store")
        self.assertEqual(resolve(url).func, store)


    def test_resolved_url_cart(self):
        url = reverse("cart")
        self.assertEqual(resolve(url).func, cart)


    def test_resolved_url_checkout(self):
        url = reverse("checkout")
        self.assertEqual(resolve(url).func, checkout)
