
def mystery(in1, in2):
    total = 0
    if len(in1) != len(in2):
        # Adjust the length of the longer list to match the shorter one
        if len(in1) > len(in2):
         in1 = in1[:len(in2)]
        else:
         in2 = in2[:len(in1)]
    for i in range(len(in1)):
        if not (in1[i]+in2[i]):
            break
        total += (in1[i]+ in2[i])
    return total

# A SECTION

# [3,4,5,6], [-7,-8,1,2] ==9
print(mystery ([3,4,5,6], [-7,-8,4,2]))

# [1,3,5,7], [3,-3,3,-3] == 4
print(mystery ([1,3,5,7], [3,-3,3,-3]))

# [1,2,3,4], [-4,-3,-2,-1] == 0
print(mystery ([1,2,3,4], [-4,-3,-2,-1]))

# [7, 1, 3, 4], [-2, 2, -3, 3] ==8 
print(mystery ([7, 1, 3, 4], [-2, 2, -3, 3]))


# B SECTION

# [1, 2, 3, 4], [3, -1, 3, -1, 5] == 14
print(mystery ([1, 2, 3, 4], [3, -1, 3, -1, 5]))


'''
#another way to solve

in1 = [1,2,3,4]
in2 = [3,-1,3,-1,4]

def mystery(in1, in2):
    total = 0
    if len(in1) != len(in2):    #added part
        in1 = in1[: len(in2)]   #added part
    else:                       #added part
        in2 = in2[: len(in1)]   #added part

    for i in range(len(in1)):
        if not(in1[i]+in2[i]):
            break
        total += (in1[i] + in2[i])
    return total


print(mystery(in1,in2))
'''
