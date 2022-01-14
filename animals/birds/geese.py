from animals.animal import Animal
from movements import Flying, Swimming, Walking

class Goose(Animal, Flying, Walking, Swimming):
    """ Class to define instances of various animals in our petting zoo
    """    
    
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Flying.__init__(self)
        Swimming.__init__(self)
        Walking.__init__(self)
    
    def honk(self): 
        print("The goose honks. A lot")

    # run is defined in the Walking parent class, but also here. This run method will take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the {self.species}'