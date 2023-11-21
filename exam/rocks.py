import random 
def throw_rock():
    x = random.randint(0,100)
    return x

player1 = []
player2 =[]

for i in range(3):
    x = 100 - throw_rock()
    player1.append(x)

    x = 100 - throw_rock()
    player2.append(x)

    if player1[i] in player1 or player1 [i] in player2 or player2[i] in player2 or player2[i] in player1:
        continue


closest_player1 = min(player1)
closest_player2 = min(player2)

if closest_player1 < closest_player2:
    print("PLAYER 1 WINS")
else:
    print("PLAYER 2 WINS")




'''
import random

player_1 = []
player_2 = []


def throw_rock():
    for i in range(3):
        player_1_distances = random.randint(1,100)
        distance_from_wall = 100 - player_1_distances
        player_1.append(distance_from_wall)


    for i in range(3):
        player_2_distances = random.randint(1,100)
        distance_from_wall = 100 - player_2_distances
        player_2.append(distance_from_wall)
        
    
throw_rock()
min_distance_1 = min(player_1)
min_distance_2 = min(player_2)


if(min_distance_1 < min_distance_2): 
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
'''



