class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "stupendous snakes of all sizes"
        self.animals = list()
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def report(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description}, like:')
        for self.animal in self.animals:
            print(f'   * {self.animal.name}')
            
    @property
    def last_critter_added(self):
        last_critter = self.animals[-1]
        return f'{last_critter.name} the {last_critter.species} was the last critter added to {self.attraction_name}.'
class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "wetlands full of feathered friends and fantastic fish"
        self.animals = list()
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def report(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description}, like:')
        for self.animal in self.animals:
            print(f'   * {self.animal.name}')
            
    @property
    def last_critter_added(self):
        last_critter = self.animals[-1]
        return f'{last_critter.name} the {last_critter.species} was the last critter added to {self.attraction_name}.'
class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def report(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description}, like:')
        for self.animal in self.animals:
            print(f'   * {self.animal.name}')
            
    @property
    def last_critter_added(self):
        last_critter = self.animals[-1]
        return f'{last_critter.name} the {last_critter.species} was the last critter added to {self.attraction_name}.'
