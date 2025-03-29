from django.contrib import admin
from galery.models import Image

class ListingImages(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Image, ListingImages)
