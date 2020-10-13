# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

mama = Llama("Mama Llama", "domestic llama")


class Goat:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

billy = Goat("Billy", "domestic goat")
        
class Donkey:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

waffles = Donkey("Waffles", "domestic donkey")

class Pig:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

chris = Pig("Chris P Bacon", "domestic pig")

class Ox:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

para = Ox("Para 'D' Ox", "domestic ox")