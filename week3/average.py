sum = 0
count = 0

number = int(input("Enter a number: "))

while number != -1:
    if count >= 3:
        print("You entered too many values!")
        break 

    if number<0:
        print("Negative values are not allowed")
        number = int(input("Enter a number: "))
        continue

    sum = sum + number
    count += 1

    number = int(input("Enter a number: "))

print("average= ",(sum/count))

'''
while number != -1:
    sum = sum + number #sum+=number
    count = count + 1  #count+=1

    number = int(input("Enter a number: "))

print(sum)
print(count)
print("average= ",(sum/count))

'''
