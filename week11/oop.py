#oop.py

import random

#Object Oriented Programming 
#Nesne Yonelimli Programlama

#constructor fonksiyon init

class Human():
    money = 2000
    bag = []
    def __init__(self, name, affiliation="N/A"):
        self.name = name
        self.affiliation = affiliation
        self.money = random.randint(1000,3000)
        self.bag = []

    def print(self):
        print("name:{}, company:{}, money:{}$".format(self.name,self.affiliation,self.money))

    def buy(self,item,cost): #Human.buy yani item ve cost icin self. demene gerek yok
        if cost <= self.money:
            self.money-=cost
            self.bag.append(item)

hm1 = Human("cihan", "ITU")
hm2 = Human("hakan", "Tiktak")
hm3 = Human("merve")

hm1.print()
hm2.print()
hm3.print()




'''names = ["cihan", "hakan", "merve"]
humans=[]
for name in names:
    humans.append(Human(name))'''






'''hm = Human() #instance olusturma hm isimli bir nesne olusturuyorsun
print(hm.bag, hm.money) 
hm.buy("elma", 500)
print(hm.bag, hm.money)'''