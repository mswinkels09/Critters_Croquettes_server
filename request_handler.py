from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import Animal, Llama, Goat, Donkey, Pig, Ox, Ratsnake, Copperhead, Python, Rattlesnake, Kingsnake, SeaTurtle, Eel, Dolphin, Shark, Whale
from attractions import PettingZoo, Wetlands, SnakePit
from datetime import date
import json


mama = Llama(1, "Mama Llama", "domestic llama","morning", "llama chow")
billy = Goat(2, "Billy", "domestic goat", "midday", "goat chow")
waffles = Donkey(3, "Waffles", "domestic donkey", "afternoon", "donkey chow")
chris = Pig(4,"Chris P Bacon", "domestic pig", "morning", "pig chow")
para = Ox(5, "Para 'D' Ox", "domestic ox", "midday", "ox chow")

dude = SeaTurtle(6, "Dude", "domestic sea turtle")
shocky = Eel(7, "Shocky", "domestic eel")
towel = Dolphin(8, "Towel", "domestic dolphin")
finn = Shark(9, "Finn", "domestic shark")
boo = Whale(10,"Boo You Whale", "domestic whale")

cheese = Ratsnake(11, "Cheese", "domestic ratsnake")
bronze = Copperhead(12, "Bronze", "domestic copperhead")
monty = Python(13, "Monty", "domestic python")
shake = Rattlesnake(14,"Shake", "domestic rattlesnake")
louis = Kingsnake(15, "King Louis", "domestic kingsnake")

varmint_village = PettingZoo("Varmint Village")
pit_of_doom = SnakePit("Pit of Doom")
waterworld = Wetlands("Waterworld")

varmint_village.add(mama)
varmint_village.add(billy)
varmint_village.add(waffles)
varmint_village.add(chris)
varmint_village.add(para)

pit_of_doom.add(cheese)
pit_of_doom.add(bronze)
pit_of_doom.add(monty)
pit_of_doom.add(shake)
pit_of_doom.add(louis)

waterworld.add(dude)
waterworld.add(shocky)
waterworld.add(towel)
waterworld.add(finn)
waterworld.add(boo)

print(mama.feed())
print(billy.feed())
print(waffles.feed())
print(chris.feed())

# for animal in varmint_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

# for animal in pit_of_doom.animals:
#     print(f'You can find {animal.name} the {animal.species} in {pit_of_doom.attraction_name}')

# for animal in waterworld.animals:
#     print(f'You can find {animal.name} the {animal.species} in {waterworld.attraction_name}')
