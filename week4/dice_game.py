#dice_game.py

import random 

def roll():
    return random.randint(1, 6)

def game(goal=100):
    count = 0
    while goal:
        z = roll()
        count += 1
        if z<=goal:
            goal -= z
    #print("You succeed with", count, "rolls")
    return count

def experiment(n=100, g=100):
    s = 0 
    for i in range(n):
        res = game(g)
        s += res
    print("Average:", s/n)

experiment(n = 10000)