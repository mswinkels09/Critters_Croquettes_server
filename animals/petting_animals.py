# import the python datetime module to help us create a timestamp
from datetime import date
from .animals import Animal

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, chip_number, name, species, shift, food ):
        super().__init__(chip_number, name, species, food)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was not fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goat(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        super().__init__(chip_number, name, species, food)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was enthusiastically fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
class Donkey(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        super().__init__(chip_number, name, species, food)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was obnoxiously fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Pig(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        super().__init__(chip_number, name, species, food)
        self.shift = shift
        self.walking = True


class Ox(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        super().__init__(chip_number, name, species, food)
        self.shift = shift
        self.walking = True