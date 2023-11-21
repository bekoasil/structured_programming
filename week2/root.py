
from math import sqrt

# a x^2 - bc + c
# d = b^2 - 4ac
# (-b-d)/2a 

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = b**2 - 4*a*c / (2*a)
x1 = (-1 * b - sqrt(d)) / (2*a)
x2 = (-1 * b + sqrt(d)) / (2*a)

print("First root:", x1)
print("First root:", x2)