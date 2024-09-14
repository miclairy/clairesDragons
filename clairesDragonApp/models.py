from django.db import models

# Create your models here.

class Dragon(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    terrian = models.CharField(max_length=10)
    fireBreather = models.BooleanField()
    waterBreather = models.BooleanField()
    eyeColor = models.CharField(max_length=10)
    armored = models.BooleanField()
    horns = models.IntegerField()
    fins = models.BooleanField()
    feathers = models.BooleanField()
    wings = models.BooleanField()
    legs = models.IntegerField()
    # url = models.CharField(max_length=200) # todo generate button for dragons etc
    

    def generate(self):
        self.save()
        
    def __str__(self):
        return self.name
        
    
    