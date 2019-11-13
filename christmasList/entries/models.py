from django.db import models
import os
from django.utils.functional import cached_property
from django.utils.html import format_html
from django_resized import ResizedImageField

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Gift(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=10000)
    price = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return  Gift.formatNoneType(self.name) + " | " + Gift.formatNoneType(self.price) + " | " + Gift.formatNoneType(self.available) 

    def formatNoneType(inString):
        if inString is None:
            return ''
        return str(inString)
        
    @cached_property
    def display_image(self):
        html = '<img src="{img}">'
        if self.image:
            return format_html(html, img=self.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')
    display_image.short_description = 'Display image'
