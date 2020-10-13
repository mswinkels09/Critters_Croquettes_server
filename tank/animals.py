# import the python datetime module to help us create a timestamp
from datetime import date

class Ratsnake:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
    
cheese = Ratsnake("Cheese", "domestic ratsnake")
        
class Copperhead:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

bronze = Copperhead("Bronze", "domestic copperhead")

class Python:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

monty = Python("Monty", "domestic python")

class Rattlesnake:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

shake = Rattlesnake("Shake", "domestic rattlesnake")

class Kingsnake:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

louis = Kingsnake("King Louis", "domestic kingsnake")