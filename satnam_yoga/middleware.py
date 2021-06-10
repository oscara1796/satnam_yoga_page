
from django.shortcuts import redirect
from django.urls import reverse
import requests

from payments.views import get_paypal_token
from users.models import  statusChoices
from django.utils import timezone

class profile_payment_completion_middleware:
    """Corrobroa si el ususario existe en profile o ya hizo signin"""
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):

        if request.path == '/payments/' and  not request.user.is_authenticated:
            return redirect('login')

        response = self.get_response(request)

        return response


# class user_profile_completion_middleware:
#     """Corrobroa si el ususario existe en profile o ya hizo signin"""
#     def __init__(self, get_response):
#         self.get_response= get_response
#
#     def __call__(self, request):
#         try:
#             if request.user.profile:
#                 if not request.user.is_staff:
#                     profile = request.user.profile
#                     if not profile.image or not profile.phone_number:
#                         if request.path  not in [reverse('update_profile'), reverse('logout'), reverse('success_payment')]:
#                             return redirect('update_profile')
#         except:
#             pass
#         response = self.get_response(request)
#
#         return response


class user_profile_paypal_account_verify_is_active_middleware:
    """Corrobroa si el ususario existe en profile o ya hizo signin"""
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        try:
            if request.user.profile:
                if not request.user.is_staff:
                    profile = request.user.profile
                    if profile.paypalSubscriptionId:
                        # print(profile.active)
                        # print(type(statusChoices.TRIAL))
                        if profile.active == "statusChoices.TRIAL":
                            # print("Hello i am in middleware")
                            suspend_date = profile.paypal_cancel_date
                            current_time = timezone.now()
                            if  current_time >= suspend_date:
                                access_token = get_paypal_token()
                                headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
                                url = f'https://api-m.paypal.com/v1/billing/subscriptions/{profile.paypalSubscriptionId}/cancel'
                                r = requests.post(url, headers=headers).json()
                                profile.delete()

        except Exception as e:
            print(f'PRINT EXCEPTION {e}')
        response = self.get_response(request)

        return response
