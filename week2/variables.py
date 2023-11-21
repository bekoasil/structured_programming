#variable.py

'''
integer (tam sayilar) -256 10 789
float - doubl(ondalikli sayilar) 4.05 100000.12 678
string (metin) "cihan" 'hakan' "alex10"
'''

x = 5 
y = 4.5
z = "bekir"
q = 4+5
w = x+y

print("_________")

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(w, type(w))

#type 
# + - * / 
print("_________")

print(4+5)
print(4-5)
print(4*5)
print(4/5)
print(4//5) #integer division
print(2**4) #power
print(43%5) #mod

print("bekir"+"asil") #concatination print("bekir"+5)
print("bekir"*2)

# print(int("cihan")) --> NOT POSSIBLE 

print("_________")

nick = "bekir" + str(x)
print(nick)

print(int("567") + 76)

print("_________")

x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)

print("_________")
#bool
a = 5 > 4
print (a,type(a))

a = 5 == 5
print (a,type(a))

print("_________")
a = 5 != 5
print (a,type(a))

b=True

print(not a) #True
print(a and b) #False
print(a or b) # True



