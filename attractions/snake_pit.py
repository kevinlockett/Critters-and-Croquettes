from .attractions import Attraction

class SnakePit(Attraction):
    
    def __init__(self, name, description):
        super().__init__(name, description)
        
        # Number 1: Duck typing check
    def add_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to hang with snakes, so please do not put it in the {self.attraction_name} attraction.')