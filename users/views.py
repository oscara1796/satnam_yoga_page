from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# ·Models

from users.models import Profile, YogaClass, DayClass
from django.contrib.auth.models import User

# Forms
from users.forms import SignupForm, ProfileForm


@login_required
def update_profile_view(request):
    profile = request.user.profile
    user = request.user
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            profile.phone_number = data['phone_number']
            profile.image = data['image']
            profile.save()

            return redirect('update_profile')

    return render(request, 'users/update_profile.html',{'profile': profile, 'user': user, 'form': form})




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
            return render(request, 'users/login.html',{'error': 'Usuario invalido o contraseña'})

    return render(request, 'users/login.html')


def logout_view(request):

    logout(request)

    return redirect('feed')



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


def classes_schedule(request):


    return render(request)
