from enum import Enum
import os

from django.shortcuts import redirect
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

class Breath(Enum):
    WATER = 'water'
    FIRE = 'fire'
    STEAM = 'steam'
    NONE = 'nothing'
    

def whatDoesItBreathe(breathesFire, breatherWater):
    if (breathesFire and breatherWater):
        return Breath.STEAM
    elif (breathesFire):
        return Breath.FIRE
    elif (breatherWater):
        return Breath.WATER
    return Breath.NONE

def boolToText(value):
    return value if 'there are' else 'there are not any'

def generate(dragon):

    response = client.images.generate( 
        model="dall-e-3",
        prompt=f"a realistic {dragon.color} dragon with {dragon.legs} legs that breathes {whatDoesItBreathe(dragon.fireBreather, dragon.waterBreather)}, they have {dragon.eyeColor} colored eyes and {dragon.horns} horns and {boolToText(dragon.fins)} fins and {boolToText(dragon.feathers)} feathers.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    print('pancake', response.data[0].url)
    return redirect(response.data[0].url)