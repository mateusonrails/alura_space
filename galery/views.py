from django.shortcuts import render, get_object_or_404
from galery.models import Image


def index(request):
    images = Image.objects.all()
    return render (request, 'galery/index.html', { 'cards': images })

def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'galery/image.html', { 'image': image })