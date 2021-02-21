"""Users forms """

#Django
from django import forms

# Models
from users.models import Profile

from django.contrib.auth.models import User

class ProfileForm(forms.Form):
    first_name= forms.CharField(max_length=100, required= True)
    last_name= forms.CharField(max_length=100, required= True)
    email = forms.EmailField( max_length=100, required= True)
    phone_number= forms.CharField(max_length=15, required= True)
    image = forms.ImageField()

class SignupForm(forms.Form):
    """Sign Up Form"""
    error_css_class = 'error'

    username = forms.CharField(
    label=False,
    min_length=4,
    max_length=50,
     widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario','class': 'form-control','required': True}))

    password = forms.CharField(
    label=False,
    max_length=70,
    widget=forms.PasswordInput(attrs={'placeholder':'Escribe tu contraseña','class': 'form-control','required': True}))

    password_confirmation = forms.CharField(
    label=False,
    max_length=70,
    widget=forms.PasswordInput(attrs={'placeholder':'Confirma tu contraseña','class': 'form-control','required': True}))

    first_name = forms.CharField(
    label=False,
    min_length=2,
    max_length=50,
    widget = forms.TextInput(attrs={'placeholder':'Nombres','class': 'form-control','required': True}))

    last_name = forms.CharField(
    label=False,
    min_length=2,
    max_length=50,
    widget = forms.TextInput(attrs={'placeholder':'Apellidos','class': 'form-control','required': True}))

    email = forms.EmailField(
    label=False,
    min_length=6,
    max_length=70,
    widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico','class': 'form-control','required': True}))

    def clean_username(self):
        """username must be unique"""

        username = self.cleaned_data['username']

        # Hacemos un query a la base de datos
        username_taken= User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya esta en uso ')
        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password= data['password']
        password_confirmation= data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data


    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        # profile = Profile(user=user)
        # profile.save()
