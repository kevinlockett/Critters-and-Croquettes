from animals.animal import Animal
from movements import Swimming

class Koi(Animal, Swimming):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)