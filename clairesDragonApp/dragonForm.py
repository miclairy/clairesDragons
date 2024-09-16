from django import forms

from .models import Dragon

class DragonForm(forms.ModelForm):

    class Meta:
        model = Dragon
        fields = ('name', 
                  'color', 
                  'terrain', 
                  'fireBreather', 
                  'waterBreather', 
                  'eyeColor', 
                  'armored',
                  'horns',
                  'fins',
                  'feathers',
                  'wings',
                  'legs'
                  )
        
        