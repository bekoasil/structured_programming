
def count(values, query):
    count = 0 
    for v in values:
        if v == query:
            count += 1 
    return count 


def remove(values, query):
    c = count(values, query)
    for i in range(c):
        values.remove(query)
    return values


my_list = [3, 5, 6, 5, 4, 1, 5, 8, 9, 6, 5]

my_list = remove(my_list, 5)

pass