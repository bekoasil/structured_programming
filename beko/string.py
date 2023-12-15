greet = r"Bekir\n" #r raw string icin kullanilir ve ozel ifadeleri de string gibi alir
print(greet)

abc = '''asdasdads 
sdfsdfsdd 
sfdsdfsf\n
        fdghjghhkjl'''  #''' ''' multi line string

print(abc)

#immutable 
a = "Bekir"
a_x = a.replace("e", "u")
print(a) #immutable oldugu icin replace fonkdan etkilenmedi
print(a_x)

for i in range(len(greet)):
    print(greet[i], end="-")
print()
print(greet[2:5])