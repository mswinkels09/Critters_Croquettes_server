# import the python datetime module to help us create a timestamp
from datetime import date
from .animals import Animal
from movements import Walking, Swimming

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, chip_number, name, species, shift, food ):
        Animal.__init__(self, chip_number, name, species, food)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was not fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
        ...
    
    def honk(self): 
        print("The goose honks. A lot")

    # run is defined in the Walking parent class, but also here. This run method will take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Goose'

class Goat(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        Animal.__init__(self, chip_number, name, species, food)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was enthusiastically fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
class Donkey(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        Animal.__init__(self, chip_number, name, species, food)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was obnoxiously fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Pig(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        Animal.__init__(self, chip_number, name, species, food)
        self.shift = shift
        self.walking = True


class Ox(Animal):
    def __init__(self, chip_number, name, species, shift, food ):
        Animal.__init__(self, chip_number, name, species, food)
        self.shift = shift
        self.walking = True