from datetime import date
from animals.animal import Animal
from movements import Walking

class Llama(Animal, Walking):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, shift, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
        
    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name}, the {self.species}, had "Rockytop" sung to it so it would eat its {self.food}.')