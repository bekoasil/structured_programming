import random

iron = 0 
copper = 0
alloy = 0
storage = 0 
max_day = 365

def mine_iron():
    iron_bar_chance = random.randint(1,5)
    if iron_bar_chance == 1:
        return 1
    else:
        return 0

def mine_copper():
    copper_bar_chance = random.randint(1, 2)
    if copper_bar_chance == 1:
        return 1
    else:
        return 0


while storage < 10:

    if mine_iron() == 1:
        iron += 1
        storage += 1

    if mine_copper() == 1:
        copper += 1
        storage += 1

    if copper >= 3 and iron >= 3:
        iron -= 3
        copper -= 3
        storage -= 6
        alloy += 1 










