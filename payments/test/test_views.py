from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from payments.models import *
import json
import os


class TestViews(TestCase):
    """docstring forTestViews."""

    def setUp(self):
        self.client = Client()
        self.payment_home_url= reverse('payment_home')
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()


    def test_payment_home_GET(self):
        self.client.force_login(user)
        response = self.client.get(self.payment_home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'payments/payment_home.html')

        
    def test_payment_home_GET(self):
        self.client.force_login(user)
        response = self.client.get(self.payment_home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'payments/payment_home.html')
