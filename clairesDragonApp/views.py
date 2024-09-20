import time
import uuid
from django.shortcuts import render
from django.http import HttpResponse

from clairesDragonApp.dragonForm import DragonForm
from clairesDragonApp.galleryImages import getImageUrl, putImage
from clairesDragonApp.generateDragon import generate

from .models import Dragon


def index(request):
    return create(request)

def about(request) :
    return render(request, 'clairesDragonApp/about.html')

def create(request):
    form = DragonForm()
    url = ''
    if (request.method == "POST"):
        form = DragonForm(request.POST)
        if (form.is_valid()):
            dragon = form.save(commit=False)
            url = generate(dragon)
            if url != None:    
                imageKey = str(uuid.uuid4())
                dragon.imageKey = imageKey
                dragon.save()
                putImage(url, imageKey)
            
    return render(request, 'clairesDragonApp/create.html', {'dragonForm': form, 'dragonUrl': url})

def gallery(request):
    dragons = Dragon.objects.all()
    urls = []
    for dragon in dragons:
        urls.append(getImageUrl(dragon.imageKey))
   
    return render(request, 'clairesDragonApp/gallery.html', {'dragons': dragons, 'imageUrls': reversed(urls)})
