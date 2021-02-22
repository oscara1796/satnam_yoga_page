from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from enum import Enum

# Create your models here.


class statusChoices(Enum):
    ACTIVE = 'ACTIVO'
    TRIAL = 'TEMPORAL'
    CANCELLED = 'CANCELADO'



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= "Usuario")

    image = models.ImageField(upload_to="user_images/", verbose_name= "Imagen");

    phone_number = models.CharField(max_length=20, blank=True, verbose_name= "Teléfono");

    active = models.CharField(max_length=1, null=False, verbose_name= "Status", choices= [(choice, choice.value) for choice in statusChoices], default=statusChoices.CANCELLED)

    stripeCustomerId = models.CharField(max_length=255, verbose_name= "Stripe Cliente id", blank=True, null= True)
    stripeSubscriptionId = models.CharField(max_length=255, verbose_name= "Stripe Subscripción id", blank=True, null= True)
    paypalSubscriptionId = models.CharField(max_length=255, verbose_name= "Paypal Subscripción id", blank=True, null= True)
    paypalPlanId = models.CharField(max_length=255, verbose_name= "Paypal plan id", blank=True, null= True)

    created = models.DateTimeField(auto_now_add= True, verbose_name= "creado");
    modified = models.DateTimeField(auto_now= True, verbose_name= "Modificado");

    class Meta:
        verbose_name= "Perfil"
        verbose_name_plural= "Perfiles"
        ordering= ['-created']

    def __str__(self):
        """return user name!"""
        return self.user.username


@receiver(pre_delete, sender=Profile)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    try:
        instance.image.delete(False)
    except:
        pass
