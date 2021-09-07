from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


class Paypal(models.Model):

    SKU = models.CharField(max_length=100, verbose_name= "SKU", blank=True, null= True)
    name = models.CharField(max_length=100, verbose_name= "Plan ", blank=True, null= True)
    description = models.TextField(verbose_name= "Descripción", blank=True, null= True)
    paypalPlanId = models.CharField(max_length=255, verbose_name= "Paypal plan id", blank=True, null= True)
    image= models.ImageField(verbose_name="Imagen", upload_to='plans', null= True)

    created = models.DateTimeField(auto_now_add= True, verbose_name= "creado");
    modified = models.DateTimeField(auto_now= True, verbose_name= "Modificado");

    class Meta:
        verbose_name= "Paypal Plan"
        verbose_name_plural= "Paypal Plans"
        ordering= ['-created']

    def __str__(self):
        """return user name!"""
        return self.name

@receiver(pre_delete, sender=Paypal)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    try:
        instance.image.delete(False)
    except:
        pass
