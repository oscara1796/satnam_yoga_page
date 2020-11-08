from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# ·Models

from users.models import Profile
from django.contrib.auth.models import User

# Forms
from users.forms import SignupForm




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


def logout_view(request):

    logout(request)

    return redirect('login')



def signup_view(request):
     """Sign up view"""
     if request.method == 'POST':
         form = SignupForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login')
     else:
         form = SignupForm()

     return render(
         request=request,
         template_name= 'users/signup.html',
         context={'form':form}
     )
