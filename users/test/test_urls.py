from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *

# Create your tests here.
class TestUrls(SimpleTestCase):
    """docstring forTestUrls."""



    def test_resolved_url_login(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, login_view)


    def test_resolved_url_logout(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout_view)


    def test_resolved_url_signup(self):
        url = reverse("signup")
        self.assertEqual(resolve(url).func, signup_view)

    def test_resolved_url_classes_schedule(self):
        url = reverse("classes_schedule")
        self.assertEqual(resolve(url).func, classes_schedule)


    def test_resolved_url_update_profile(self):
        url = reverse("update_profile")
        self.assertEqual(resolve(url).func, update_profile_view)
