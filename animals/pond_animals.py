
# import the python datetime module to help us create a timestamp
from datetime import date

class SeaTurtle:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"


    
class Eel:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dolphin:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Shark:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Whale:
    def __init__(self, chip_number, name, species):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"
