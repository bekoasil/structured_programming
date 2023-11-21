'''
n = 5

Output =
*
**
***
****
*****


'''

n = 1

while n<=5:
    print("*"*n)
    n += 1

print("_____")


n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

print("______")


n = 6
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print("*", end="")
    print("")

print("______")


