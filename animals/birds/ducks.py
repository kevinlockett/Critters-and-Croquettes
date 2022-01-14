from animals.animal import Animal
from movements import Flying, Swimming, Walking

class Duck(Animal, Flying, Swimming, Walking):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Flying.__init__(self)
        Swimming.__init__(self)
        Walking.__init__(self)