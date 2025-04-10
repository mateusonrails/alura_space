from django.urls import path
from apps.galery.views import index, image, search

urlpatterns = [
    path('', index ,name="index"),
    path('image/<int:image_id>', image, name="image"),
    path('search', search, name="search")
]