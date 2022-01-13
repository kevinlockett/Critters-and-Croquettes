from birds import Chicken, Duck, Eagle, Heron, Peafowl
from fishes import Catfish, Characin, Cichlid, Goldfish, Koi
from mammals import Alpaca, Beaver, Donkey, Goat, Lamb, Llama, Pig
from reptiles import Copperhead, Cobra, Garter_snake, Kingsnake, Python, Rat_snake, Rattlesnake, Turtle
from attractions import SnakePit, Wetlands, PettingZoo

slither_inn = SnakePit("The Slither Inn") 
varmint_village = PettingZoo("Varmint Village")
critter_cove = Wetlands("Critter Cove")

roberto = Alpaca("Roberto", "Huacaya Alpaca", "hay", "morning")
varmint_village.add_animal(roberto)

buckey = Beaver("Buckey","North American Beaver", "bark and cambium")
critter_cove.add_animal(buckey)

felix = Catfish("Felix", "Flathead Catfish", "brine shrimp, mysis shrimp, and bloodworms")
critter_cove.add_animal(felix)

figaro = Catfish("Figaro", "Blue Catfish", "brine shrimp, mysis shrimp, and bloodworms")
critter_cove.add_animal(figaro)

garfield = Catfish("Garfield", "Channel Catfish", "brine shrimp, mysis shrimp, and bloodworms")
critter_cove.add_animal(garfield)

drumstick = Chicken("Drumstick", "Rhode Island Red Chicken", "corn, oats, and blueberries")
varmint_village.add_animal(drumstick)

foghorn_leghorn = Chicken("Foghorn Leghorn", "leghorn rooster", "cracked corn")
varmint_village.add_animal(foghorn_leghorn)

kung_pao = Chicken("Kung Pao", "Rhode Island Red Chicken", "corn, oats, and blueberries")
varmint_village.add_animal(kung_pao)

margaret = Chicken("Margaret Hatcher", "Barred Plymouth Rock Chicken", "corn, oats, and blueberries")
varmint_village.add_animal(margaret)

bitey = Cobra("Bitey", "Indian Cobra", "1 rat and 2 garter snakes")
varmint_village.add_animal(bitey)

fango = Copperhead("Fango", "Northern Copperhead", "1 mouse and 10 cicadas")
slither_inn.add_animal(fango)

medusa = Copperhead("Medusa", "Northern Copperhead", "1 mouse and 10 cicadas")
slither_inn.add_animal(medusa)

dominick = Donkey("Dominick", "miniature donkey", "midday", "barley hay")
varmint_village.add_animal(dominick)

stinky = Donkey("Stinky", "miniature donkey", "afternoon", "barley hay")
varmint_village.add_animal(stinky)

daffy = Duck("Daffy","Gadwell", "corn and minnows")
varmint_village.add_animal(daffy)

donald = Duck("Donald","American Black Duck", "corn and minnows")
varmint_village.add_animal(donald)

daisy = Duck("Daisy","Blue Winged Teal", "corn and minnows")
varmint_village.add_animal(daisy)

david = Duck("David","Mallard", "corn and minnows")
varmint_village.add_animal(david)

pilot = Eagle("Pilot", "Bald Eagle", "sardines, salmon, and rabbit meat")
critter_cove.add_animal(pilot)

buzz = Eagle("Buzz", "Golden Eagle", "corn and minnows")
critter_cove.add_animal(buzz)

gertie = Garter_snake("Gertie", "Common Garter Snake", "12 earthworms")
varmint_village.add_animal(gertie)

norman = Goat("Norman", "Boehr", "hay and mixed vegetables", "afternoon")
varmint_village.add_animal(norman)

vincent = Goat("Vincent van Goat", "pygmy goat", "hay and mixed vegetables", "morning")
varmint_village.add_animal(vincent)

scape = Goat("Scape Goat", "fainting goat", "hay and mixed vegetables", "afternoon")
varmint_village.add_animal(scape)

swooney = Goat("Swooney Goat", "fainting goat", "hay and mixed vegetables", "afternoon")
varmint_village.add_animal(swooney)

butt_head = Goat("Butt-Head", "Alpine goat", "hay and mixed vegetables", "morning")
varmint_village.add_animal(butt_head)

billy = Goat("Billy the Kid", "LaMancha goat", "hay and mixed vegetables", "afternoon")
varmint_village.add_animal(billy)

finny = Goldfish("Finny", "Common Goldfish", "flaked fish food")
critter_cove.add_animal(finny)

splash = Goldfish("Splash", "Common Goldfish", "flaked fish food")
critter_cove.add_animal(splash)

heronione = Heron("Heronione", "Great Blue Heron", "sardines")
critter_cove.add_animal(heronione)

theron = Heron("Theron", "Grey Heron", "sardines")
critter_cove.add_animal(theron)

sheron = Heron("Sheron", "Pacific Heron", "sardines")
critter_cove.add_animal(sheron)

jafar = Kingsnake("Jafar", "California Mountain Kingsnake", "1 mouse")
slither_inn.add_animal(jafar)

bashful = Koi("Bashful", "Kohaku Koi", "flaked food and ground worms")
critter_cove.add_animal(bashful)

flirtatious = Koi("Flirtatious", "Taisho Sanshoku", "flaked food and ground worms")
critter_cove.add_animal(flirtatious)

kitten = Koi("Kitten", "Showa Sanshoku", "flaked food and ground worms")
critter_cove.add_animal(kitten)

reticent = Koi("Reticent", "Showa Sanshoku", "flaked food and ground worms")
critter_cove.add_animal(reticent)

skittish = Koi("Skittish", "Taisho Sanshoku", "flaked food and ground worms")
critter_cove.add_animal(skittish)

carp_e_diem = Koi("Carp-e-Diem", "Kohaku Koi", "flaked food and ground worms")
critter_cove.add_animal(carp_e_diem)

snowflake = Lamb("Snowflake", "Australian White", "sheep feed mixed with legumes and forbs", "morning")
varmint_village.add_animal(snowflake)

alan = Lamb("Alan", "Hampshire Sheep", "sheep feed mixed with legumes and forbs", "afternoon")
varmint_village.add_animal(alan)

al_paca = Llama("Al Paca", "Alpaca", "hay", "morning")
varmint_village.add_animal(al_paca)

boots = Llama("Boots", "Wooly llama", "hay", "afternoon")
varmint_village.add_animal(boots)

linda = Llama("Linda", "Domesticated llama", "hay", "afternoon")
varmint_village.add_animal(linda)

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "hay", "midday")
varmint_village.add_animal(miss_fuzz)

rainbow = Peafowl("Rainbow", "Indian Peafowl", "corn, blueberries, and ground worms")
varmint_village.add_animal(rainbow)

nancy = Peafowl("Nancy Beth Carlson", "Green Peafowl", "corn, blueberries, and ground worms")
varmint_village.add_animal(nancy)

piglet = Pig("Piglet", "Hanford Mini Swine", "pig feed mixed with corn and soy beans", "morning")
varmint_village.add_animal(piglet)

waddles = Pig("Waddles", "American Mini Pig", "pig feed mixed with corn and soy beans", "afternoon")
varmint_village.add_animal(waddles)

wilber = Pig("Wilber", "Pot-bellied Pit", "pig feed mixed with corn and soy beans", "midday")
varmint_village.add_animal(wilber)

miss_piggy = Pig("Miss Piggy", "Ossabaw Island Hog", "pig feed mixed with corn and soy beans", "morning")
varmint_village.add_animal(miss_piggy)

piggly_wiggly = Pig("Piggly Wiggly", "Meishan Breed Pig", "pig feed mixed with corn and soy beans", "afternoon")
varmint_village.add_animal(piggly_wiggly)

porky = Pig("Porky", "Juliana Breed Pid", "pig feed mixed with corn and soy beans", "afternoon")
varmint_village.add_animal(porky)

bacon = Pig("Bacon", "Pot-Bellied Pig", "pig feed mixed with corn and soy beans", "morning")
varmint_village.add_animal(bacon)

slinky = Python("Slinky", "Indian Python", "1 rat")
slither_inn.add_animal(slinky)

basil = Rat_snake("Basil", "Eastern Rat Snake", "1 mouse")
slither_inn.add_animal(basil)

slithers = Rattlesnake("Slithers", "Eastern Diamondback", "1 mouse and 10 cicadas")
slither_inn.add_animal(slithers)

rattles = Rattlesnake("Rattles", "Prairie Rattlesnake", "1 mouse and 10 cicadas")
slither_inn.add_animal(rattles)

paul_bunyon = Rattlesnake("Paul Bunyon", "Timber Rattlesnake", "1 mouse and 10 cicadas")
slither_inn.add_animal(paul_bunyon)

diablo = Rattlesnake("Diablo", "Horned Rattlesnake", "1 mouse and 10 cicadas")
slither_inn.add_animal(diablo)

crush = Turtle("Crush", "Common Snapping Turtle", "minnows, ground worms, and crayfish bits")
critter_cove.add_animal(crush)

squirtle = Turtle("Squirtle", "Mississippi Map Turtle", "midge larvae, carrion, and mollusk blend")
critter_cove.add_animal(squirtle)

rocky = Cichlid("Rocky", "Blue Umbee Cichlid", "fish pellets and minnows")
critter_cove.add_animal(rocky)

jaws = Characin("Jaws", "Black Pau", "fruit, seeds, carrots, and zucchini")
critter_cove.add_animal(jaws)

print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
squirtle.feed()
print(foghorn_leghorn)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')
    
for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')
    
for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')
    
varmint_village.report()
slither_inn.report()
critter_cove.report()