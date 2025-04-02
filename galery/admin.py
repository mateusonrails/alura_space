from django.contrib import admin
from galery.models import Image

class ListingImages(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category', 'user')
    list_editable = ('published',)
    list_per_page = 10

admin.site.register(Image, ListingImages)
