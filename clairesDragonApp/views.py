from django.shortcuts import render
from django.http import HttpResponse

from clairesDragonApp.dragonForm import DragonForm
from clairesDragonApp.generateDragon import generate
from .models import Dragon


def index(request):
    dragons = Dragon.objects.all()
    
    dragon = dragons[0]

    dragonUrls = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSVEr5UKVhHIgIZNetHnzNjogzZvZvvJTKNA&s',
                'static/clairesDragonApp/images/purpleDragon.png',
                  'https://oaidalleapiprodscus.blob.core.windows.net/private/org-9pMbbb61J0DDJ6qYQu5oefM4/user-K6Ykb8YL2njruV5ShTW872d3/img-YXVKKhQ3gtpgBhD2uHSRxEzD.png?st=2024-09-13T15%3A57%3A27Z&se=2024-09-13T17%3A57%3A27Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-12T23%3A18%3A28Z&ske=2024-09-13T23%3A18%3A28Z&sks=b&skv=2024-08-04&sig=7yhFItqDy1jT/yACXzdZZynEiO2ToA09ubuKStFvbF4%3D']

    return render(request, 'clairesDragonApp/dragons.html', {'dragons': dragonUrls})

def about(request) :
    return render(request, 'clairesDragonApp/about.html')

def create(request):
    form = DragonForm()
    if (request.method == "POST"):
        form = DragonForm(request.POST)
        if (form.is_valid()):
            dragon = form.save(commit=True)
            generate(dragon)
            
    return render(request, 'clairesDragonApp/create.html', {'dragonForm': form})
