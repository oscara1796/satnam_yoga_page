from django.db import models

# Create your models here.


class Video(models.Model):

    title = models.CharField(max_length= 100)

    image = models.ImageField(upload_to="user_images/");
    upload = models.FileField(upload_to='video_uploads/', default='default_value')

    created = models.DateTimeField(auto_now_add= True);
    modified = models.DateTimeField(auto_now= True);

    def __str__(self):
        """return user name!"""
        return self.title
