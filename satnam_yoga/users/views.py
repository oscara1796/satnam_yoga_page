from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# ·Models

from users.models import Profile
from django.contrib.auth.models import User




def login_view(request):
    """Login View"""
    if request.method == 'POST':
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user);
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error': 'Invalid username and password'})

    return render(request, 'users/login.html')
