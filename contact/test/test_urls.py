from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from contact.views import *


class TestURLS(SimpleTestCase):
    """docstring forTestURLS."""


    def test_resolver_url_contact(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func, contact)
