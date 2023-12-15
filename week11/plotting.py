#plotting.py 

import random
from matplotlib import pyplot as plt 

x = []
for i in range(100):
    x.append(random.randint(0,100))

w = 5
y = [5,5,5,5]
for i in range(100-5+1):
    y.append(sum(x[i:i+5])/5)

plt.title("Random Values")
plt.plot(x, label="data", color="blue") #cizgi grafik olusturur
plt.plot(y, label="average", color="red")

x.sort()
plt.plot(x, label="data_sorted", color="magenta")
plt.legend()
plt.show() 
plt.savefig("line_graph.png")



plt.cla()

plt.bar(x)
plt.show()



