# guess.py 
import random

def roll():
    return random.randint(1, 100)


secret = roll()
print(secret)


guess = int(input("Guess the number: "))

count = 1 
flag = False

while guess != secret:
    if count == 10:
        flag = True
        print("You lost!")
        break
    if guess > secret:
        print("DECREASE")
        guess = int(input("Guess the number: "))
    elif guess < secret: 
        print("INCREASE")
        guess = int(input("Guess the number: "))
    count += 1
print("BINGO")

    
    
 


