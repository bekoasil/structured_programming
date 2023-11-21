text = "1g4re7a3t"
sum = 0
msg =""

for letter in text:
    if letter.isdigit():
        letter = int(letter)
        sum += letter
    else: 
        msg += letter

print(msg + str(sum))