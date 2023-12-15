
a = input("Enter a value: ")

b = 6 
c = 0

try: #dener hata yoksa trydan cikar devam eder varsa except e duser devam eder
    c = int(a) + b 
except:
    print("An error occured")


print(c)