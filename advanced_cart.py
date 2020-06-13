# advanced_cart.py
import datetime
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

sales_tax_rate = float(os.getenv("sales_tax_rate"))

time = datetime.datetime.now()
now = time.strftime("%Y-%m-%d-%I-%M-%S-%f")
today = time.strftime("%Y-%m-%d %I:%M %p")

csv_filepath = os.path.join((os.path.dirname(__file__)), "data", "products.csv")

product = pd.read_csv(csv_filepath)

product_num = len(product) + 1

products = product.to_dict("records")

def to_usd(my_price):
    return f"${my_price:,.2f}"

shopping_list = []

print("Enter Product IDs to populate at list of all of the customers shopping cart items.")
print("Once completed, enter 'Done' to proceed.")
while True:
    try:
        response = input("Please Enter Product ID: ")
        if response.capitalize() == "Done":
            break
        else:
            response = int(response)
    except ValueError:
        print("Invalid Product ID")
    else:
        if response <= 0 or response >= product_num:
            print("Invalid Product ID")
        elif str([x["per_pound"] for x in products if x["id"] == response]).strip("['").strip("']") == "Y":
            try:
                pound = float(input("Please Enter Number of Pounds: "))
                shopping_list.append({"id":response,"per_pound":pound})
            except ValueError:
                print("Invalid Pound Value, Re-Enter Product ID and Try Again")
        else:
            shopping_list.append({"id":response,"per_pound":"N"})

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
        if x["id"] == i["id"] and i["per_pound"] == "N":
            print(f"... {x['name']} ({to_usd(x['price'])})")
            subtotal += float(x["price"])
        elif x["id"] == i["id"]:
            print(f"... {x['name']} ({to_usd(float(x['price'])*float(i['per_pound']))})")
            subtotal += float(x["price"]) * float(i["per_pound"])

print("---------------------------------")
print(f"SUBTOTAL: {to_usd(subtotal)}")
tax = to_usd(subtotal * sales_tax_rate)
total = to_usd(subtotal * (1 + sales_tax_rate))
print(f"TAX: {tax}")
print(f"TOTAL: {total}")
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), "receipts", f"{now}.txt")

with open(file_name, "w") as file:
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
            if x["id"] == i["id"] and i["per_pound"] == "N":
                file.write(f"... {x['name']} ({to_usd(x['price'])})")
                file.write("\n")
            elif x["id"] == i["id"]:
                file.write(f"... {x['name']} ({to_usd(float(x['price'])*float(i['per_pound']))})")
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