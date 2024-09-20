import time
from django.shortcuts import render
from django.http import HttpResponse

from clairesDragonApp.dragonForm import DragonForm
from clairesDragonApp.galleryImages import galleryImages
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
            dragon = form.save(commit=True)
            # url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-9pMbbb61J0DDJ6qYQu5oefM4/user-K6Ykb8YL2njruV5ShTW872d3/img-juzuEM4scEKEyDjA9wShwZZi.png?st=2024-09-16T13%3A36%3A33Z&se=2024-09-16T15%3A36%3A33Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-15T23%3A17%3A55Z&ske=2024-09-16T23%3A17%3A55Z&sks=b&skv=2024-08-04&sig=SQ4fMcr4bcsjYQkj0YpFpd1rNzvxbZ/aoQwls0Y/bMw%3D'
            # url = 'static/clairesDragonApp/images/purpleDragon.png'
            url = generate(dragon)
            
    return render(request, 'clairesDragonApp/create.html', {'dragonForm': form, 'dragonUrl': url})

def gallery(request):
    dragons = Dragon.objects.all()
    url = galleryImages()
    return render(request, 'clairesDragonApp/gallery.html', {'dragons': dragons, 'url': url})
