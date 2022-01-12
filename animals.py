# import the python datetime module to help us create a timestamp
from datetime import date

class Donkey:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        
dominick = Donkey("Dominick", "miniature donkey")

class Llama:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        
miss_fuzz = Llama("Miss Fuzz", "domestic llama")
boots = Llama("Boots", "Wooly llama")

class Goat:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        
vincent = Goat("Vincent van Goat", "pygmy goat")
scape = Goat("Scape Goat", "fainting goat")
butt_head = Goat("Butt-Head", "Alpine goat")
billy = Goat("Billy the Kid", "LaMancha goat")
        
class Pig:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        
piglet = Pig("Piglet", "Hanford Mini Swine")
waddles = Pig("Waddles", "American Mini Pig")
wilber = Pig("Wilber", "Mulefoot Hog")
miss_piggy = Pig("Miss Piggy", "Ossabaw Island Hog")
piggly_wiggly = Pig("Piggly Wiggly", "Meishan Breed Pig")
porky = Pig("Porky", "Juliana Breed Pid")
bacon = Pig("Bacon", "Pot-Bellied Pig")
        
class Lamb:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        
snowflake = Lamb("Snowflake", "Australian White")
alan = Lamb("Alan", "Hampshire Sheep")
        
class Copperhead:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        
medusa = Copperhead("Medusa", "Northern Copperhead")
        
class Rat_snake:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        
basil = Rat_snake("Basil", "Eastern Rat Snake")
        
class Kingsnake:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

jafar = Kingsnake("Jafar", "California Mountain Kingsnake")
        
class Python:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        
slinky = Python("Slinky", "Indian Python")
        
class Rattlesnake:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        
slithers = Rattlesnake("Slithers", "Eastern Diamondback")
rattles = Rattlesnake("Rattles", "Prairie Rattlesnake")
paul_bunyon = Rattlesnake("Paul Bunyon", "Timber Rattlesnake")
diablo = Rattlesnake("Diablo", "Horned Rattlesnake")
        
class Duck:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        
daffy = Duck("Daffy", "Gadwell")
donald = Duck("Donald", "American Black Duck")
daisy = Duck("Daisy", "Blue Winged Teal")
david = Duck("David", "Mallard")

class Goldfish:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        
finny = Goldfish("Finny", "Common Goldfish")
splash = Goldfish("Splash", "Common Goldfish")
        
class Beaver:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        
buckey = Beaver("Buckey", "North American Beaver")
        
class Catfish:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        
felix = Catfish("Felix", "Flathead Catfish")
figaro = Catfish("Figaro", "Blue Catfish")
garfield = Catfish("Garfield", "Channel Catfish")

class Turtle:
    """ Class to define instances of various animals in our petting zoo
    """

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        
crush = Turtle("Crush", "Common Snapping Turtle")
squirtle = Turtle("Squirtle", "Mississippi Map Turtle")

print(garfield.species)


