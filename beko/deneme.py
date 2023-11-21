list = [3, 5 ,7, 9, 1, 4, 7]
target = 16


def check_sum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return True
    return False

print(check_sum(list, target))


