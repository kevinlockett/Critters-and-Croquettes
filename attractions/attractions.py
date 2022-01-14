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
    
    def report(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description}, like:')
        for self.animal in self.animals:
            print(f'   * {self.animal.name}')
            
    @property
    def last_critter_added(self):
        last_critter = self.animals[-1]
        return f'{last_critter.name} the {last_critter.species} was the last critter added to {self.attraction_name}.'