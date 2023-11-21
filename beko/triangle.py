

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("")

print("_______")

for i in range(5, 0, -1): #5, 4, 3, 2, 1, 0
    for j in range(i): 
        print("*", end="")
    print("")