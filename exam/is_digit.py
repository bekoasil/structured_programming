text = "1c4i7ha3n"


sum = 0

for letter in text: 
    if letter.isdigit():
        letter = int(letter) #this is the missing part
        sum += letter
print(sum)

