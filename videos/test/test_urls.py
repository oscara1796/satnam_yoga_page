from django.test import SimpleTestCase
from django.urls import reverse, resolve
from videos.views import *

# Create your tests here.
class TestUrls(SimpleTestCase):
    """docstring forTestUrls."""



    def test_resolved_url_feed(self):
        url = reverse("feed")
        self.assertEqual(resolve(url).func, list_menu)


    def test_resolved_url_video_list_menu(self):
        url = reverse("video_list_menu")
        self.assertEqual(resolve(url).func, categories_list)


    def test_resolved_url_category(self):
        url = reverse("category", args=["1"])
        self.assertEqual(resolve(url).func, category)

    def test_resolved_url_video_id_show(self):
        url = reverse("video_id_show", args=["1", "2"])
        self.assertEqual(resolve(url).func, video_id_show)
