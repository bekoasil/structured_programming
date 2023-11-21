import random

max_storage = 10

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

def simulate(max_day, iron_worker, copper_worker):
    iron = 0 
    copper = 0
    profit = 0

    for i in range(max_day):
        for j in range(iron_worker):
            iron += mine_iron()
        for j in range(copper_worker):
            copper += mine_copper()
        while iron >= 3 and copper >= 3:
            iron -= 3
            copper -= 3
            profit += 13 

        if iron > max_storage:
            profit += (iron - 5) * 1
            iron = 5
        
        if copper > max_storage:
            profit += (copper - 5) * 0.5
            copper = 5
    profit += iron * 1
    profit += copper * 0.5

    return profit 

def estimate_profit(n, max_day, iron_worker, copper_worker):
    total_profit = 0
    for i in range(n):
        total_profit += simulate(max_day, iron_worker, copper_worker)
        average_profit = total_profit / n 
    return average_profit

print("Iron Worker: 1, Copper Worker: 4, Profit:", estimate_profit(1000,365,1,4))
print("Iron Worker: 2, Copper Worker: 3, Profit:", estimate_profit(1000,365,2,3))
print("Iron Worker: 3, Copper Worker: 2, Profit:", estimate_profit(1000,365,3,2))
print("Iron Worker: 4, Copper Worker: 1, Profit:", estimate_profit(1000,365,4,1))      
    











