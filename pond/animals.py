# import the python datetime module to help us create a timestamp
from datetime import date

class SeaTurtle:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

dude = SeaTurtle("Dude", "domestic sea turtle")

    
class Eel:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

shocky = Eel("Shocky", "domestic eel")

class Dolphin:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

towel = Dolphin("Towel", "domestic dolphin")

class Shark:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

finn = Shark("Finn", "domestic shark")

class Whale:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

boo = Whale("Boo You Whale", "domestic whale")
