from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Image
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    images = Image.objects.order_by('date_photograph').filter(published=True)

    return render (request, 'galery/index.html', { 'cards': images })

def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'galery/image.html', { 'image': image })

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')

        return redirect('login')

    images = Image.objects.order_by('date_photograph').filter(published=True)

    if "search" in request.GET:
        search_name = request.GET['search']
        if search_name:
            images = images.filter(name__icontains=search_name)

    return render(request, 'galery/search.html', { 'cards': images })

def new_image(request):
    return render(request, 'galery/new_image.html')

def edit_image(request):
    pass

def delete_image(request):
    pass