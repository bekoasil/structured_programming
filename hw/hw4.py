#hw4 cashier 
sold_items = {}

while True:
    print("1. Sell")
    print("2. Checkout")

    user_input = input("Make a choice: ")
    user_input = int(user_input)

    if user_input < 1 or user_input > 2:
        print("Wrong input")
        continue
    elif user_input == 2:
        print("End of the Day")
        print("Sold items: ")
        break
    else:
        sold_item = input("Enter the sold item: ")
        amount = input("How many sold: ")
        amount = int(amount)
       
        if sold_item in sold_items.keys():
            sold_items[sold_item] += amount
        else:
            sold_items[sold_item]= amount
        print(amount, sold_item, "sold.")

for k,v in sold_items.items():
    print(f"{v:<5}{k:>5}")




