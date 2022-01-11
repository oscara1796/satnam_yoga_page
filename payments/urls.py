from django.urls import path
from . import views as payments_views


urlpatterns = [
    path('payments/', payments_views.HomePagePaymentView , name="payment_home"),
    path('payments/success/', payments_views.SuccessPaymentView , name="success_payment"),
    path('payments/cancelled/', payments_views.CancelledPaymentView , name="cancelled_payment"),
    path('payments/subs_cancelled/', payments_views.Cancelled_or_Reactivate_SubscriptionView , name="cancelled_subscription"),
    path('config/', payments_views.stripe_config),
    path('create-checkout-session/', payments_views.create_checkout_session),
]
