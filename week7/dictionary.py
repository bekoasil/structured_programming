


client1 = {"name": "bekir", "age": 29, "score": 65}
print(client1)

client1["employed"] = True
client1["age"] = 27
client1["cars"] = ["Mazda MX-5"]
print(client1)


client1.pop("name") #name'i ucurur
print(client1)

del client1["age"]
print(client1) #age'i ucurur

str = "________\n"

print(str)

for k in client1.keys():
    print(k)
print(str)
for i in client1.items():
    print(i)
print(str)
for k,v in client1.items():
    print(k, "->", v)


print(str)
if "job" in client1.keys():
    print(client1["job"])
else:
    client1["job"] = "unemployed"
print(client1)