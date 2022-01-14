from datetime import date
from animals import Animal
class Rattlesnake(Animal):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
        
    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name} the {self.species} was fed {self.food} immediately after a venom milking demonstration.')