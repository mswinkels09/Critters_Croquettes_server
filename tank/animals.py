# import the python datetime module to help us create a timestamp
from datetime import date

class Ratsnake:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
        
class Copperhead:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Python:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Rattlesnake:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Kingsnake:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

