
def detect_star (values):
    for i in range(len(values)):
        if values[i]>5:
            values[i]=0
    return values

my_list = [3, 5, 4, 8, 9, 3, 2, 6]
print("Original list:", my_list)
print("Detected star list:", detect_star(my_list.copy()))
