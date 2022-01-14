from animals.animal import Animal
from movements import Walking

class Duck(Animal, Walking):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)