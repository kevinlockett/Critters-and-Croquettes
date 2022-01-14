from animals import Animal
class Pig(Animal):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True