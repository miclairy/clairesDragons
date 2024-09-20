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
            # url = 'https://dragon-images.s3.amazonaws.com/img-hk6W3YFem90GyKIy82eFDAD3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAXBZV5EHQP5FSHAE4%2F20240920%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240920T205009Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=2f3bbb564b9aca3c4c967728f646be0a0c8bbd6f60de2ce0ab1b7661298a922e'
            # url = 'static/clairesDragonApp/images/purpleDragon.png'
            dragon = form.save(commit=False) # pancake don't forget to store the imageKey
            url = generate(dragon)
            if url != None:    
                imageKey = str(uuid.uuid4())
                dragon.imageKey = imageKey
                dragon.save()
                putImage(url, imageKey)
            
    return render(request, 'clairesDragonApp/create.html', {'dragonForm': form, 'dragonUrl': url})

def gallery(request):
    dragons = Dragon.objects.all()
    url = getImageUrl('img-bPbi2DPYdr4mv6Q0lLUdoZK6')
   # url = getImageUrl('img-hk6W3YFem90GyKIy82eFDAD3.png')
    imageKey = str(uuid.uuid4())
    print(imageKey, 'pancake image key')
   # putImage('https://dragon-images.s3.eu-north-1.amazonaws.com/img-8xZSg6kH7wTkcCMafxC7IHiV.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCmV1LW5vcnRoLTEiRjBEAiBUA%2FWfdKB4yxvvakU%2BfmRttshZZhK1XxbCaL9dvl2W5QIgNt%2FAnqzujDXO9XEOe1O%2FRfPI7a3oKkOPOPYEQt%2F8qvgq6AIIfhAAGgw0ODQ5MDc0OTE4MDgiDJb4Y9ehjXNcUvrK2SrFAlFA3TrRkq8pZIl%2BVWLzhrWBKK194OZTuysxkUZ6Xw1H0KhjrmaoBm4Jotrl2zAjhxQHkh%2Bk%2BiU5qLs0%2BNmdokqO%2BpHEE0XYU%2BB5GagyfRVlHPW9VoOjb6r%2FVJmL2NvwlH7sZIgZ3R9LEkYL9bNbmxUh7KvIU9L6M33b7juFbv1lzac1OSRd%2B%2B6GMlnEakrax4VM3G1xlxwO1dJ2hc33iz8ujVTadWmNDAPDxrcmqPj57NmFdnO6ctXGHShIIXQVWkviqIiFT2ospJWcYa%2FGoAu%2FGJeWxSq40TTBeCqlzlCA5wSZLGlVjgSiCNI9zQ4SkftheFW%2BsT4rGa8MhpSG%2F0ApAwEKD2xFhL89GnHNhGZfSgBq8c%2B%2FqKFc2Qu5AXrjZlgGtEYNNB89OhmVsQTdBJOFhoeboUVW%2B8nn3dYGWv%2BEb2hYg7swq5W3twY6tALxgGRXbYeot%2F8yg1Okc71vE%2BmsYfNBI9KTkRuJJPjjFdAWNnJWJgr0vZrSjhqkQBT8YgywgZ1lJWDXdMp%2BaEA4kuQTX3KCsOg7qwkdNPPXnUp5OUym3fAMeTrYr5ui%2BntO6O5a%2Bm6OR%2FaFHpu07lCcf%2FmiQ5z58NJsllbVWKMKdacn3iS7l%2BPUapoVdG%2BAynegZB2q21qQX7l3c6FyEEiscF3t9%2BiGyQl75qbOSCXIQ9tMSWUF9cfsiHJnTPeBCpHB9v47ZQMm%2B74ci0WiMHhM6SjMLetkDJ6xQ7EFSDzxj%2FNyLmUsRJwKstRkjP4FNvfOLdet4bEZNcvHjJJRFWfeHwsKRM0lZJ9ncSoTqgFYLhAqoASl6534vgFadx5a0ibtVe2oTSASFQQXb6heFv455W1lgA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240920T212641Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAXBZV5EHQIJBGCLYR%2F20240920%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=4edd1f1c65e690c26b697856393ca3aa6c5df8f7d0ee356c574b8be1c374ae8b', imageKey)
   
    return render(request, 'clairesDragonApp/gallery.html', {'dragons': dragons, 'url': url})
