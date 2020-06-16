# Shopping Cart Project

## Functionality

This checkout system has a few different programs depending on the level of complexity that the cashier would like to use. The basic functionality that is common across all three programs is that the cashier can enter the Product IDs of the items in a customer's shopping cart and the program will do the following:

* Automatically Lookup Prices
* Perform Tax & Total Calculations
* Print A Customer Receipt

The second level of the program will also create a .txt file of the customers receipt. Additionally, you will be able to set a specific sales tax rate based upon your location.

The third level of the program will also accept products that are priced per pound and use a products directory from a CSV file rather than being hard-coded.

## Setup

### Repo Setup

Use [GitHub](https://github.com/minipele06/shopping-cart-exercise) to clone the project repository called "Shopping Cart Exercise". Use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

>cd ~/Desktop/shopping-cart-exercise

### Environment Setup

Create and activate a new Anaconda virtual environment:

>conda create -n shopping-env python=3.7 # (first time only)

>conda activate shopping-env

From within the virtual environment, install the required packages specified in the "requirements.txt" file:

>pip install -r requirements.txt

### Sales Tax Rate Setup

You will then need to create a .env file to save your specific sales tax rate which should be labeled sales_tax_rate.

>sales_tax_rate=0.0875

## Instructions

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

>python app/shopping_cart.py

If you receive a message to enter your customers shopping cart item IDs, then you have properly set up the program and may proceed.

In order to run the second level program, run the following python script from the command-line:

>python app/enhanced_cart.py

In order to run the third level program, run the following python script from the command-line:

>python app/advanced_cart.py

## Step-By-Step Guide

As stated above, once you receive a message to enter your Product IDs, you are ready to use the program. 

You may enter as many Product IDs as are necessary. Once you've completed entering in all of the customers Product IDs, type 'Done' the next time the program prompts you to enter a Product ID. Your Product IDs will be validated to exclude any Product ID that doesn't exist. Additionally, if the product is priced per pound, the third level program will ask the cashier how many pounds the customer is purchasing. 

The list of products and product information will be below for the first and second program. 

>{"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
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

For the third program, the list of products can be viewed and edited in the csv file in the data folder labeled products.csv.

Once you have entered 'Done', the program will proceed to creating the customer receipt. If you are running the second level or third level program, it will also save a receipt .txt file. 

Finally, the program will also print out a customer receipt.