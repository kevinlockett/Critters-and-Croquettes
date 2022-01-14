from birds import Chicken, Duck, Eagle, Heron, Peafowl
from fishes import Catfish, Characin, Cichlid, Goldfish, Koi
from mammals import Alpaca, Beaver, Donkey, Goat, Lamb, Llama, Pig
from reptiles import Anaconda, Copperhead, Cobra, Garter_snake, Kingsnake, Python, Rat_snake, Rattlesnake, Turtle
from attractions import SnakePit, Wetlands, PettingZoo

slither_inn = SnakePit("The Slither Inn") 
varmint_village = PettingZoo("Varmint Village")
critter_cove = Wetlands("Critter Cove")

roberto = Alpaca("Roberto", "Huacaya Alpaca", "hay", "morning", 453876)
varmint_village.add_animal(roberto)

buckey = Beaver("Buckey","North American Beaver", "bark and cambium", 42905)
critter_cove.add_animal(buckey)

felix = Catfish("Felix", "Flathead Catfish", "brine shrimp, mysis shrimp, and bloodworms", 63350)
critter_cove.add_animal(felix)

figaro = Catfish("Figaro", "Blue Catfish", "brine shrimp, mysis shrimp, and bloodworms", 2943)
critter_cove.add_animal(figaro)

garfield = Catfish("Garfield", "Channel Catfish", "brine shrimp, mysis shrimp, and bloodworms", 63895)
critter_cove.add_animal(garfield)

drumstick = Chicken("Drumstick", "Rhode Island Red Chicken", "corn, oats, and blueberries", 30744)
varmint_village.add_animal(drumstick)

foghorn_leghorn = Chicken("Foghorn Leghorn", "leghorn rooster", "cracked corn", 92607)
varmint_village.add_animal(foghorn_leghorn)

kung_pao = Chicken("Kung Pao", "Rhode Island Red Chicken", "corn, oats, and blueberries", 26810)
varmint_village.add_animal(kung_pao)

margaret = Chicken("Margaret Hatcher", "Barred Plymouth Rock Chicken", "corn, oats, and blueberries", 44812)
varmint_village.add_animal(margaret)

bitey = Cobra("Bitey", "Indian Cobra", "1 rat and 2 garter snakes", 76426)
varmint_village.add_animal(bitey)

fango = Copperhead("Fango", "Northern Copperhead", "1 mouse and 10 cicadas", 71893)
slither_inn.add_animal(fango)

medusa = Copperhead("Medusa", "Northern Copperhead", "1 mouse and 10 cicadas", 97310)
slither_inn.add_animal(medusa)

dominick = Donkey("Dominick", "miniature donkey", "midday", "barley hay", 67443)
varmint_village.add_animal(dominick)

stinky = Donkey("Stinky", "miniature donkey", "afternoon", "barley hay", 87603)
varmint_village.add_animal(stinky)

daffy = Duck("Daffy","Gadwell", "corn and minnows", 41482)
varmint_village.add_animal(daffy)

donald = Duck("Donald","American Black Duck", "corn and minnows", 32254)
varmint_village.add_animal(donald)

daisy = Duck("Daisy","Blue Winged Teal", "corn and minnows", 53599)
varmint_village.add_animal(daisy)

david = Duck("David","Mallard", "corn and minnows", 33526)
varmint_village.add_animal(david)

pilot = Eagle("Pilot", "Bald Eagle", "sardines, salmon, and rabbit meat", 61628)
critter_cove.add_animal(pilot)

buzz = Eagle("Buzz", "Golden Eagle", "corn and minnows", 55048)
critter_cove.add_animal(buzz)

gertie = Garter_snake("Gertie", "Common Garter Snake", "12 earthworms", 70479)
varmint_village.add_animal(gertie)

norman = Goat("Norman", "Boehr", "hay and mixed vegetables", "afternoon", 38314)
varmint_village.add_animal(norman)

vincent = Goat("Vincent van Goat", "pygmy goat", "hay and mixed vegetables", "morning", 31862)
varmint_village.add_animal(vincent)

scape = Goat("Scape Goat", "fainting goat", "hay and mixed vegetables", "afternoon", 17356)
varmint_village.add_animal(scape)

swooney = Goat("Swooney Goat", "fainting goat", "hay and mixed vegetables", "afternoon", 66298)
varmint_village.add_animal(swooney)

butt_head = Goat("Butt-Head", "Alpine goat", "hay and mixed vegetables", "morning", 87244)
varmint_village.add_animal(butt_head)

billy = Goat("Billy the Kid", "LaMancha goat", "hay and mixed vegetables", "afternoon", 44491)
varmint_village.add_animal(billy)

finn = Goldfish("Finny", "Common Goldfish", "flaked fish food", 123789)
critter_cove.add_animal(finn)

splash = Goldfish("Splash", "Common Goldfish", "flaked fish food", 64032)
critter_cove.add_animal(splash)

heronione = Heron("Heronione", "Great Blue Heron", "sardines", 29423)
critter_cove.add_animal(heronione)

theron = Heron("Theron", "Grey Heron", "sardines", 7357)
critter_cove.add_animal(theron)

sheron = Heron("Sheron", "Pacific Heron", "sardines", 98906)
critter_cove.add_animal(sheron)

jafar = Kingsnake("Jafar", "California Mountain Kingsnake", "1 mouse", 66392)
slither_inn.add_animal(jafar)

bashful = Koi("Bashful", "Kohaku Koi", "flaked food and ground worms", 53496)
critter_cove.add_animal(bashful)

flirtatious = Koi("Flirtatious", "Taisho Sanshoku", "flaked food and ground worms", 81289)
critter_cove.add_animal(flirtatious)

kitten = Koi("Kitten", "Showa Sanshoku", "flaked food and ground worms", 28345)
critter_cove.add_animal(kitten)

reticent = Koi("Reticent", "Showa Sanshoku", "flaked food and ground worms", 9522)
critter_cove.add_animal(reticent)

skittish = Koi("Skittish", "Taisho Sanshoku", "flaked food and ground worms", 37041)
critter_cove.add_animal(skittish)

carp_e_diem = Koi("Carp-e-Diem", "Kohaku Koi", "flaked food and ground worms", 59315)
critter_cove.add_animal(carp_e_diem)

snowflake = Lamb("Snowflake", "Australian White", "sheep feed mixed with legumes and forbs", "morning", 23025)
varmint_village.add_animal(snowflake)

alan = Lamb("Alan", "Hampshire Sheep", "sheep feed mixed with legumes and forbs", "afternoon", 98966)
varmint_village.add_animal(alan)

al_paca = Llama("Al Paca", "Alpaca", "hay", "morning", 96290)
varmint_village.add_animal(al_paca)

boots = Llama("Boots", "Wooly llama", "hay", "afternoon", 86789)
varmint_village.add_animal(boots)

linda = Llama("Linda", "Domesticated llama", "hay", "afternoon", 5248)
varmint_village.add_animal(linda)

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "hay", "midday", 63099)
varmint_village.add_animal(miss_fuzz)

rainbow = Peafowl("Rainbow", "Indian Peafowl", "corn, blueberries, and ground worms", 86404)
varmint_village.add_animal(rainbow)

nancy = Peafowl("Nancy Beth Carlson", "Green Peafowl", "corn, blueberries, and ground worms", 61773)
varmint_village.add_animal(nancy)

piglet = Pig("Piglet", "Hanford Mini Swine", "pig feed mixed with corn and soy beans", "morning", 65065)
varmint_village.add_animal(piglet)

waddles = Pig("Waddles", "American Mini Pig", "pig feed mixed with corn and soy beans", "afternoon", 64075)
varmint_village.add_animal(waddles)

wilber = Pig("Wilber", "Pot-bellied Pit", "pig feed mixed with corn and soy beans", "midday", 57042)
varmint_village.add_animal(wilber)

miss_piggy = Pig("Miss Piggy", "Ossabaw Island Hog", "pig feed mixed with corn and soy beans", "morning", 15825)
varmint_village.add_animal(miss_piggy)

piggly_wiggly = Pig("Piggly Wiggly", "Meishan Breed Pig", "pig feed mixed with corn and soy beans", "afternoon", 44986)
varmint_village.add_animal(piggly_wiggly)

porky = Pig("Porky", "Juliana Breed Pid", "pig feed mixed with corn and soy beans", "afternoon", 51502)
varmint_village.add_animal(porky)

bacon = Pig("Bacon", "Pot-Bellied Pig", "pig feed mixed with corn and soy beans", "morning", 11921)
varmint_village.add_animal(bacon)

slinky = Python("Slinky", "Indian Python", "1 rat", 62518)
slither_inn.add_animal(slinky)

basil = Rat_snake("Basil", "Eastern Rat Snake", "1 mouse", 34606)
slither_inn.add_animal(basil)

slithers = Rattlesnake("Slithers", "Eastern Diamondback", "1 mouse and 10 cicadas", 10374)
slither_inn.add_animal(slithers)

rattles = Rattlesnake("Rattles", "Prairie Rattlesnake", "1 mouse and 10 cicadas", 76354)
slither_inn.add_animal(rattles)

paul_bunyon = Rattlesnake("Paul Bunyon", "Timber Rattlesnake", "1 mouse and 10 cicadas", 60268)
slither_inn.add_animal(paul_bunyon)

diablo = Rattlesnake("Diablo", "Horned Rattlesnake", "1 mouse and 10 cicadas", 27021)
slither_inn.add_animal(diablo)

crush = Turtle("Crush", "Common Snapping Turtle", "minnows, ground worms, and crayfish bits", 27411)
critter_cove.add_animal(crush)

squirtle = Turtle("Squirtle", "Mississippi Map Turtle", "midge larvae, carrion, and mollusk blend", 45445)
critter_cove.add_animal(squirtle)

rocky = Cichlid("Rocky", "Blue Umbee Cichlid", "fish pellets and minnows", 43184)
critter_cove.add_animal(rocky)

jaws = Characin("Jaws", "Black Pau", "fruit, seeds, carrots, and zucchini", 72564)
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

print(finn.chip_number)

# This should not change the state of the object
finn.chip_number = 555783

# But printing it should work
print(finn.chip_number)

sammy = Anaconda("Sammy", "Green Anaconda", "tapir", 357896)
slither_inn.add_animal(sammy)

shalene = Rat_snake("Shalene", "Yellow Rat Snake", "1 rat", 453552)
slither_inn.add_animal(shalene)

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(critter_cove.last_critter_added)