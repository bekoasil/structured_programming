# descision.py
#if - elif - else

'''
if exp1
    runs if exp1 true
elif exp2
    runs if exp2 true
elif exp3 
    runs if exp3 true
else 
    if all exps are false
'''

secret = 4
guess = int(input("guess the number"))

if guess < secret:
    print("Go Up")
elif guess > secret:
    print("Go Down")
else:
    print("Bingo")