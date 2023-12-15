a = ["aa", "bb", "cc", "dd"]

print("{name} is {age} years old.".format(name="cihan", age=30))

my_str = "".join(a)
print(my_str)


my_str = "--".join(a)
print(my_str)

data = "30,25,67,85,26"
print(data)
data = data.split(",")
print(data)

for i in range(len(data)):  
    data[i] = int(data[i])  #listenin icindeki degerleri int'e cevir 

print(data)

print("____\n")
for v in data:
    a.append(int(v))
data = a
print(data)

#list comprehension
#data_list = [int(v) for v in data]


