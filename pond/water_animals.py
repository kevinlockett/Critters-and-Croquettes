from datetime import date

class Water_animal:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, type, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.type = type
        self.species = species
        self.swimming = True
        self.date_added = date.today()