from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="user_images/");

    phone_number = models.CharField(max_length=20, blank=True);

    active = models.BooleanField(default=False, null=False)

    stripeCustomerId = models.CharField(max_length=255, null= True)
    stripeSubscriptionId = models.CharField(max_length=255, null= True)

    created = models.DateTimeField(auto_now_add= True);
    modified = models.DateTimeField(auto_now= True);

    def __str__(self):
        """return user name!"""
        return self.user.username
