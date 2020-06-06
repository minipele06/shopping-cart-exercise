# shopping_cart.py
import datetime

import os

time = datetime.datetime.now()
now = time.strftime("%Y-%m-%d-%I-%M-%S-%f")
today = time.strftime("%Y-%m-%d %I:%M %p")
# time = datetime.strptime("6:56", "%H:%M")
# time = datetime.strftime("%I:%M" %p)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

shopping_list = []

print("Enter Product IDs to populate at list of all of the customers shopping cart items.")
print("Once completed, enter 'Done' to proceed.")
while True:
    try:
        response = input("Please Enter Product ID: ")
        if response == "Done":
            break
        else:
            response = int(response)
    except ValueError:
        print("Invalid Product ID")
    else:
        if response <= 0 or response >= 21:
            print("Invalid Product ID")
        else:
            shopping_list.append(response)

print("---------------------------------")
print("Best Foods Grocery")
print("WWW.BEST-FOODS-GROCERY.COM")
print("---------------------------------")
print(f"CHECKOUT AT: {today}")
print("---------------------------------")
print("SELECTED PRODUCTS:")
subtotal = 0

for i in shopping_list:
    for x in products:
        if x["id"] == i:
            print(f"... {x['name']} ({to_usd(x['price'])})")
            subtotal += float(x["price"])

print("---------------------------------")
print(f"SUBTOTAL: {to_usd(subtotal)}")
tax = to_usd(subtotal * 0.0875)
total = to_usd(subtotal * 1.0875)
print(f"TAX: {tax}")
print(f"TOTAL: {total}")
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

# file_name = "my_message.txt"

file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), "receipts", f"{now}.txt")


with open(file_name, "w") as file: # "w" means "open the file for writing"
    file.write("---------------------------------")
    file.write("\n")
    file.write("Best Foods Grocery")
    file.write("\n")
    file.write("WWW.BEST-FOODS-GROCERY.COM")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write(f"CHECKOUT AT: {today}")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write("SELECTED PRODUCTS:")
    file.write("\n")
    for i in shopping_list:
        for x in products:
            if x["id"] == i:
                file.write(f"... {x['name']} ({to_usd(x['price'])})")
                file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write(f"SUBTOTAL: {to_usd(subtotal)}")
    file.write("\n")
    file.write(f"TAX: {tax}")
    file.write("\n")
    file.write(f"TOTAL: {total}")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write("THANKS, SEE YOU AGAIN!")
    file.write("\n")
    file.write("---------------------------------")