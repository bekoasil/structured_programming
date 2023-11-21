list = [1, 2, 3, 4, 5]


def reverse(list):
    new_list = []
    for i in range((len(list)-1), -1, -1):
        new_list.append(list[i])
    return new_list

new_list = reverse(list)
print(new_list)

