
n = 6
for i in range(n):
    print("*"*n)
    n -= 1
    

print("Enter a number: ")
n = int(input())

def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")

        for j in range(i+1):
            print("*", end="")
        print("")

print(pattern(n))