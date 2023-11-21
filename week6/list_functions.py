#list_functions.py

my_list = []

my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(9)
my_list.append(7)

i = my_list.index(3) #aradigin deger hangi indexte

my_list.insert(2,97)

for i in range(my_list.count(7)):
    my_list.remove(7)

my_list.remove(7)

my_list.clear()


