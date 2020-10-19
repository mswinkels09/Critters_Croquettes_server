class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    @property
    def last_critter_added(self):
        return f'Last animal added was {self.animals[-1]}'

class SnakePit(Attraction):
    def __init__(self, name, description):
        self.description = "cute and scaley critters"
        self.animals = list()

class Wetlands(Attraction):
    def __init__(self, name, description):
        self.description = "cute and wet critters"
        self.animals = list()

