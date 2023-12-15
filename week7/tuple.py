#tuple.py

#list
a  = [3, 5, 5.5, "cihan", [1,3]]
#if 5.5 in a 
#remove del 
#sort ()

#tuple
b = (3, 5, "hakan")
#tuple degistirilemez
#tuple eleman eklenemez, cikarilamaz 

print(a)
print(b)

a.append(67) #you can not append any thing to tuple
print(a)

a = a + [67]
print(a)

print(a[2]) # list 0 - 1 - 2.elemanini getirir
print(b[1]) # tuple 0 - 1.elemanini getirir

str = "__________________________\n"

print(str)


client = []

client.append(["cihan", 30, 75])
client.append(["hakan", 45, 62])
client.append(["merve", 25, 45])
print(client)

print(str)

limit = 60 
counter = 0 
for c in client:
    name, age, score = c
    if score >= limit: 
        counter +=1 

print(counter, "clients has at least", limit, "score.")

print(str)

name = input("Name: ")
age = input("Age: ")
score = age + 10

client.append((name, age, score))
