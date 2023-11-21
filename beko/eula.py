print("... kontrat ...")
answer = str(input("Do you accept EULA? (y/n): "))

while answer != "y" and answer != "n":
    print("You must enter whether y or n!")
    answer = str(input("Do you accept EULA? (y/n): "))
        
if answer == "y":
    print("You accepted EULA")
elif answer == "n":
    print("You seclined EULA")