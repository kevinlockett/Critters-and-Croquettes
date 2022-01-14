from datetime import date
from animals import Animal
class Llama(Animal):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
        
    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name}, the {self.species}, had "Rockytop" sung to it so it would eat its {self.food}.')