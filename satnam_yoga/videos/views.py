from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.


@login_required
def list_menu(request):

    return render(request, 'videos/feed.html')
