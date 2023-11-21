current_year = 2023 
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
if age >= 50:
    print("OLD")
else:
    print("YOUNG")