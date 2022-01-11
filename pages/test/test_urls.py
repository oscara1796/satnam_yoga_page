from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import *
# Create your tests here.

class TestURLS(SimpleTestCase):
    """for urls in """


    def test_page_view_url_is_resolved(self):
        url = reverse("page", args=["1","some-slug"])
        self.assertEquals(resolve(url).func, page_view)
