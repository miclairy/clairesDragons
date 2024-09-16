from django.shortcuts import render
from django.http import HttpResponse

from clairesDragonApp.dragonForm import DragonForm
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
            url = generate(dragon)
            
    return render(request, 'clairesDragonApp/create.html', {'dragonForm': form, 'dragonUrl': url})
