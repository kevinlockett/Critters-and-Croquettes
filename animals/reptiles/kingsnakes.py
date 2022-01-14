from animals.animal import Animal
from movements import Slithering

class Kingsnake(Animal, Slithering):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)