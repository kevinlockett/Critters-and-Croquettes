from datetime import date
from animals import Animal
class Eagle(Animal):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.flying = True
        
    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name}, the {self.species}, was fed {self.food} during a live exhibition.')
    