


def pay(money,level):
    global a
    payment = 3000 + level*500
    money += payment
    a = "rich"
    return money
 
a = "bekir"
money = 100
pay(money,3)   

print("My money:", money)