"""POSTS MODELS"""

from django.db import models
from django.utils.timezone import now
# Create your models here.
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add= True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now= True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"
        ordering= ['created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title= models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    published= models.DateTimeField(verbose_name="Contenido", default=now)
    image= models.ImageField(verbose_name="Imagen", upload_to='blog')
    author= models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category,verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add= True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now= True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name= "Post"
        verbose_name_plural= "Posts"
        ordering= ['created']

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Post)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    try:
        instance.image.delete(False)
    except:
        pass
