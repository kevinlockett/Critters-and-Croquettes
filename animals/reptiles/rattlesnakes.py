from datetime import date
from animals.animal import Animal
from movements import Slithering

class Rattlesnake(Animal, Slithering):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        
    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name} the {self.species} was fed {self.food} immediately after a venom milking demonstration.')