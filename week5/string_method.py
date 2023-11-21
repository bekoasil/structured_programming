
name = "bekir"
lastName = 'asil'

big_name = name.upper()
up_name = name.title()

new_name = name[0].upper() + name[1:-1] + name[-1].upper()

print(big_name)
print(up_name)
print(new_name)

name = name.upper()

if 'a' in name.lower():
    print("Uyuman lazim")
if 'eki' in name.lower(): 
    print("Adamsin")
if 'e' in name.lower():
    print("Aslansin")

msg = "   c@nim$   "
print(msg)
msg = msg.replace("@","a")
print(msg)
msg = msg.replace("$","s")
print(msg)

#msg.strip()
msg = msg.rstrip() #rstrip sagdaki bosluklari yok eder
print(msg)

msg = msg.lstrip() #lstrip soldaki bosluklari yok eder
print(msg)

msg = msg.strip() #strip tum bosluklari yok eder
print(msg)

sname = "selena"
s = sname*3
print(s)