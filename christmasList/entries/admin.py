from django.contrib import admin

from .models import Gift

# Register your models here.
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'link', 'available', 'image', 'display_image')

admin.site.register(Gift, GiftAdmin)
