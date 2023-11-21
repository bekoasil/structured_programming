#exr1.py BMI Calculator

boy = float(input("Boyunuzu giriniz (m): "))
kilo = int(input("Kilonuzu giriniz (kg): "))

BMI = kilo / (boy**2) 
print("BMI skorun= " ,BMI)

if 20< BMI < 25:
    print("Boy Kilo oranin IYI")
else:
    print("Boy Kilo oranin KOTU")