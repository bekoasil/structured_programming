
list1 = []
list2 = []
arr1 = []
arr2 = []

max_len_1 = 5
max_len_2 = 4

def append_to_list(list, integer):
        list.append(integer)

for i in range(max_len_1):
    integer = int(input("Enter an integer (list1): "))
    append_to_list(list1, integer)

for i in range(max_len_2):
    integer = int(input("Enter an integer (list2): "))
    append_to_list(list2, integer)

print(list1)
print(list2)


def crop(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            arr1 = arr1[:len(arr2)]
        else: 
            arr2 = arr2[:len(arr1)]



crop(list1, list2)
print(list1)
print(list2)
