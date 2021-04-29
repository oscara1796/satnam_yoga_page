from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name= "Nombre")
    created = models.DateTimeField(auto_now_add= True);
    modified = models.DateTimeField(auto_now= True);

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"
        ordering= ['-created']

    def __str__(self):
        """return video name!"""
        return self.name

class Video(models.Model):

    title = models.CharField(max_length= 100, verbose_name= "Titulo")

    image = models.ImageField(upload_to="user_images/", verbose_name= "Imagen", blank= True);
    categories= models.ManyToManyField(Category, verbose_name="Categorias")
    upload = models.TextField(verbose_name= "Vimeo embeded")
    description = RichTextField(verbose_name="Contenido")
    free_seen= models.BooleanField(default=False, null=False, verbose_name= "Muestra gratis")
    created = models.DateTimeField(auto_now_add= True);
    modified = models.DateTimeField(auto_now= True);

    class Meta:
        verbose_name= "Video"
        verbose_name_plural= "Vídeos"
        ordering= ['created']

    def __str__(self):
        """return video name!"""
        return self.title

@receiver(pre_delete, sender=Video)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    try:
        instance.image.delete(False)
        instance.upload.delete(False)
    except:
        instance.upload.delete(False)
