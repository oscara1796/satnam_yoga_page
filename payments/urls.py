from django.urls import path
from . import views as payments_views


urlpatterns = [
    path('payments/', payments_views.HomePagePaymentView , name="payment_home"),
    path('payments/success/', payments_views.SuccessPaymentView , name="success_payment"),
    path('payments/cancelled/', payments_views.CancelledPaymentView , name="cancelled_payment"),
    path('payments/subs_cancelled/', payments_views.Cancelled_or_Reactivate_SubscriptionView , name="cancelled_subscription"),
    path('payments/suspend_paypal/', payments_views.suspend_paypal_View , name="suspend_paypal_sub"),
    path('payments/reactivate_paypal/', payments_views.reactivate_paypal_View , name="reacti_paypal_sub"),
    path('config/', payments_views.stripe_config),
    path('create-checkout-session/', payments_views.create_checkout_session),
    path('webhook/', payments_views.stripe_webhook),
    path('webhook/paypal/', payments_views.webhook_paypal),
]
