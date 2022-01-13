from datetime import date

class Donkey:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species, food, shift):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        self.food = food
        self.shift = shift
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
    def __str__(self):
        return f"{self.name} is a {self.species}"