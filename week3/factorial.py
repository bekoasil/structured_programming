# 5! = 1,2,3,4,5

result = 1

n = int(input("Enter n: "))

for x in range(1,1+n): #[1,2,3,n]
    result *= x

print(result)