from django.db import models
import os
from django.utils.functional import cached_property
from django.utils.html import format_html
from django_resized import ResizedImageField
from PIL import Image
import PIL
from django.utils.six import StringIO

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Gift(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=10000)
    price = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=get_image_path, default = '/photos/None/noimage.PNG')
    available = models.BooleanField(default=True)

    def __str__(self):
        return  Gift.formatNoneType(self.name) + " | " + Gift.formatNoneType(self.price) + " | " + Gift.formatNoneType(self.available)

    def formatNoneType(inString):
        if inString is None:
            return ''
        return str(inString)