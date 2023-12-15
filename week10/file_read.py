#file.py
import os
#print(os.getcwd())
#os.chdir("week10")
#print(os.getcwd())

'''
number = fp.read(9)
fp.read(1)
name = fp.read(5)
print(number,name)
'''
'''
for i in range(10):
    line = fp.readline()[:-1]
    strs = line.split(" ")
    if len(strs)<=1:
        break
    number = strs[0]
    name = strs[1]
    print(number,name)
'''

fp = open("week10\\students.txt")
data = fp.readlines()
print(data)
for d in data:
    if d[-1]=='\n':
        d = d[:-1]
    number,name,grade = d.split(" ")
    print(number,name,grade)
fp.close()

def averageFile(filepath):
    with open(filepath) as fp:
        data = fp.readlines()
        total = 0
        count = 0
        for d in data:
            if d[-1]=='\n':
                d = d[:-1]
            _,_,grade = d.split(" ")
            total+=int(grade)
            count+=1
        return total/count

avg = averageFile("week10/students.txt")
print(avg)