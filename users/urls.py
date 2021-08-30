from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import  PasswordResetForm
from . import views as users_views


urlpatterns = [
    path('users/login/', users_views.login_view, name="login"),
    path('users/logout/', users_views.logout_view, name="logout"),
    path('users/signup/', users_views.signup_view, name="signup"),
    path('users/schedule/', users_views.classes_schedule, name= "classes_schedule"),
    path('users/me/update_profile', users_views.update_profile_view, name= "update_profile"),

    path('users/reset_password/',
     auth_views.PasswordResetView.as_view(html_email_template_name='users/email_reset_template.html', template_name="users/password_reset.html", form_class=  PasswordResetForm),
     name="reset_password"),

    path('users/reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
        name="password_reset_done"),

    path('users/reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),
     name="password_reset_confirm"),

    path('users/reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_complete"),

]
