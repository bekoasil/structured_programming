
print("Enter the tax rate (0.0X): ")
tax_rate = float(input())

print("Enter the product's price: ")
price = int(input())


def add_tax(tax_rate, price):
    tax = price  * tax_rate
    tax_added_price = price + tax
    return tax_added_price

print("The price with tax is going to be: ", add_tax(tax_rate, price))
