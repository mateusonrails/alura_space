from django.shortcuts import render, get_object_or_404
from galery.models import Image


def index(request):
    images = Image.objects.order_by('date_photograph').filter(published=True)
    return render (request, 'galery/index.html', { 'cards': images })

def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'galery/image.html', { 'image': image })

def search(request):
    images = Image.objects.order_by('date_photograph').filter(published=True)

    if "search" in request.GET:
        search_name = request.GET['search']
        if search_name:
            images = images.filter(name__icontains=search_name)

    return render(request, 'galery/search.html', { 'cards': images })