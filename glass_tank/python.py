from datetime import date

class Python:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()