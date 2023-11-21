'''
1. fonksiyonun ismi*
2. fonksiyonun girdisi
3. fonksiyonun govdesi*
4. fonksiyonun cevabi

def name(inputs):
    #fonksiyonun govdesi
    return output

func isimleri sayi iceremez
ozel karakter kullanilmaz
camelCase kullanilir 


'''

def info():
    print("This is an education example")
    print("Use it with your own risk")



def minimum(o1, o2):
    if o1 < o2:
        return o1
    else:
        return o2

def greet(name="Noname"): #name= ile default deger verdik
    if name == "Bekir":
        name = "El - patron"
    print("Hello", name, "welcome!")

info()
a = 46
b = 32

c = minimum(a, b)
d = minimum(o2=57, o1=21)
#x = minimum(3, 5) direk sayi da verilebilir
info()
greet("Bekir")
greet("Sultan")
greet()

pass





