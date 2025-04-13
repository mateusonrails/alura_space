from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Image
from apps.galery.forms import ImageForms
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
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = ImageForms
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem cadastrada!')
            return redirect('index')

    return render(request, 'galery/new_image.html', {'form': form})

def edit_image(request, image_id):
    image = Image.objects.get(id=image_id)
    form = ImageForms(instance=image)

    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')


    return render(request, 'galery/edit_image.html', {'form': form, 'image_id': image_id} )

def delete_image(request, image_id):
    image = Image.objects.get(id=image_id)
    image.delete()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('index')

    