class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'Last animal added was {self.animals[-1]}'

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and scaley critters"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and wet critters"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

