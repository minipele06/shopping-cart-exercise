# Shopping Cart Project

## Functionality

This checkout system has a few different programs depending on the level of complexity that the cashier would like to use. The basic functionality that is common across all three programs is that the cashier can enter the Product IDs of the items in a customer's shopping cart and the program will do the following:

* Automatically Lookup Prices
* Perform Tax & Total Calculations
* Print A Customer Receipt

The second level of the program will also create a .txt file of the customers receipt.

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

Once you have entered 'Done', the program will proceed to creating the customer receipt. If you are running the second level or third level program, it will also save a receipt .txt file. 

Finally, the program will also print out a customer receipt.