#students.py

#listede [isim, yas, not]

school = []

school.append(["cihan", "30", 70.6])
school.append(["hakan", "35", 87.1])
school.append(["merve", "18", 56.3])
school.append(["kerem", "26", 96.8])
school.append(["aylin", "19", 95.2])

def best_student(mylist):  # bu tarz orneklerin farkli varyasyonlarini calis SINAVDA cikabilir
    best_grade = 0
    best_name = ""
    for student in mylist:
        if student[2] > best_grade:
            best_grade = student[2]
            best_name = student[0]
    return best_name

print("Your best student is:", best_student(school))




def all_pass(cluster, pass_note): # Boolean 50 ve uste ise true / false 
    for i in range(len(cluster)):
        note = cluster[i][2]
        if (note < pass_note):
            return False
    return True


a = all_pass(school, 80)
print("Are all students pass the class: ", a)






'''
for student in school:
    print(student[0])

print(" ")

for i in range(len(school)):
    print(school[i][0])
'''
