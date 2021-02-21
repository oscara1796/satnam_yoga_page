
from django.shortcuts import redirect
from django.urls import reverse

class profile_payment_completion_middleware:
    """Corrobroa si el ususario existe en profile o ya hizo signin"""
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):

        if request.path == '/payments/' and  not request.user.is_authenticated:
            return redirect('login')

        response = self.get_response(request)

        return response


class user_profile_completion_middleware:
    """Corrobroa si el ususario existe en profile o ya hizo signin"""
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        try:
            if request.user.profile:
                if not request.user.is_staff:
                    profile = request.user.profile
                    if not profile.image or not profile.phone_number:
                        if request.path  not in [reverse('update_profile'), reverse('logout'), reverse('success_payment')]:
                            return redirect('update_profile')
        except:
            pass
        response = self.get_response(request)

        return response
