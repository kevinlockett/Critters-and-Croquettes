from .attractions import Attraction
from movements import Flying, Walking

class Wetlands(Attraction):
    
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def add_animal(self, animal):
        try:
            if animal.swim_speed > -1 or animal.fly_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like hang with gators, so please do not put it in the {self.attraction_name} attraction.')