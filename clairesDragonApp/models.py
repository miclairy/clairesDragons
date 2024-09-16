from django.db import models

class Dragon(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    terrain = models.CharField(max_length=10)
    fireBreather = models.BooleanField()
    waterBreather = models.BooleanField()
    eyeColor = models.CharField(max_length=10)
    armored = models.BooleanField()
    horns = models.IntegerField()
    fins = models.BooleanField()
    feathers = models.BooleanField()
    wings = models.BooleanField()
    legs = models.IntegerField()
    url = models.CharField(max_length=200)

    def generate(self):
        self.save()
        
    def __str__(self):
        return self.name
        
    