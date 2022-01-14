from datetime import date

class Characin:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species, food, chip_num):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_num # setting the privately scoped attribute on instantiation
                
    @property # The getter
    def chip_num(self):
        return self.__chip_number
    
    @chip_num.setter # The setter
    def chip_number(self, number):
        pass
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
    def __str__(self):
        return f"{self.name} is a {self.species}"