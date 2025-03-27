from django.shortcuts import render
from galery.models import Image


def index(request):
    data = {
        1: { 'name': 'Nebulosa de Carina', 'caption': 'Webtelescope.org / NASA / James Webb'},
        2: { 'name': 'Galáxia NGC 1079', 'caption': 'nasa.org / NASA / Hubble'}
    }

    return render (request, 'galery/index.html', { 'cards': data })

def image(request):
    return render(request, 'galery/image.html')