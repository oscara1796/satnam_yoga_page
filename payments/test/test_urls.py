from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from payments.views import *

# Create your tests here.


class TestURLS(SimpleTestCase):
    """test urls for payments """

    def test_paymentHome_url_is_resolved(self):
        url = reverse("payment_home");
        self.assertEquals(resolve(url).func, HomePagePaymentView)

    def test_success_payment_url_is_resolved(self):
        url = reverse("success_payment");
        self.assertEquals(resolve(url).func, SuccessPaymentView)

    def test_cancelled_payment_url_is_resolved(self):
        url = reverse("cancelled_payment");
        self.assertEquals(resolve(url).func, CancelledPaymentView)

    def test_cancelled_subscription_url_is_resolved(self):
        url = reverse("cancelled_subscription");
        self.assertEquals(resolve(url).func, Cancelled_or_Reactivate_SubscriptionView)
