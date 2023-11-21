#list.py

empty_list = []  #creation

grades = [56, 43, 78, 2, 76, 14]

print(grades)

#indexing slacing
print(grades[1])
print(grades[-3])
print(grades[2:4])

a = len(grades)
print(a)

print(type(grades))

student = ["bekir", 30, 70.5]


weather = [25.4, 23.7, 22.9, 21.3, 24.5, 19.8, 18.6]
#iterable 

total = 0
for w in weather:
    print(w) 
    total += w
average = total / len(weather)
print("Average: {:.2f} centigrad degrees".format(average)) #formatting string / :.2f ile kac basamak decimal yazacak onu belirledik


total = 0 
for i in range(7):
    total += weather[i]
    print("{}. Day:{:.2f} C".format(i+1,weather[i]))
average = total/ len(weather)
print("Average: {:.2f} centigrad degrees".format(average))

total = 0 
for i,w in enumerate(weather):
    print(i+1, ".", w, "celcius degrees")