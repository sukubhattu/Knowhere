from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.image_name
