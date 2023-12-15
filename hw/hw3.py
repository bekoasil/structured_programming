#hw3 decodeText

key = "the quick brown fox jumps over the lazy dog"
code = [7, 12, 11, 11, 2, 7, 0]

def decodeText(key, code):
    decoded_list = []
    for i in code:
        decoded_list.append(key[i])
    a = ""    
    for j in decoded_list:
        a += j
    return a

print(decodeText(key ,code))