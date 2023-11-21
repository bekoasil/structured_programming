# Write a function that takes a list of numbers and returns a new list with all duplicates removed

def remove_duplicates(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                list.remove(list[i])
    return list

list = [1, 2, 3, 5, 7, 9, 2, 3]
print(remove_duplicates(list))



