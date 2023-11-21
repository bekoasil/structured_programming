#take a list and find the sum of even numbers 


def sum_of_evens(list):
    sum = 0
    for item in list:
        if (item % 2) == 0:
            sum += item
    return sum

list = [1, 3, 5, 8, 16, 5]
print(sum_of_evens(list))


