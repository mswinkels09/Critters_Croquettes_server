# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:
    def __init__(self, chip_number, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Goat:
    def __init__(self, chip_number, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

        
class Donkey:
    def __init__(self, chip_number, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.__chip_number = chip_number
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


class Pig:
    def __init__(self, chip_number, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


class Ox:
    def __init__(self, chip_number, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.chip_number = chip_number
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
