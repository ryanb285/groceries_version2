import os
import operator
from dotenv import load_dotenv
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

TAX_RATE = os.getenv("TAX")
STORE_WEBSITE = os.getenv("WEBSITE")
STORE_NAME = os.getenv("STORE")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS_ENV")
SENGRID_API_KEY = os.getenv("SENGRID_API_KEY_ENV")
# couldn't get the email to work but tried to set it up

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
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("Please input a product ID or type 'DONE' ")

now = datetime.now()
date_time = now.strftime("%Y-%m-%d, %H:%M")
#adapted from - https://www.programiz.com/python-programming/datetime/strftime

allowed_ids = str([id["id"] for id in products])
#adapted from Brian Stauffer

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please select a valid product ID: ")
    if selected_id.upper() == "DONE":
        break
    elif selected_ids == "":
        print("Not a valid ID, please enter a valid ID") #adapted from Brian Stauffer
    elif selected_id in allowed_ids:
        selected_ids.append(selected_id)
    else:
        print("Not a valid ID, please enter a valid ID")
        

print("-------------------")
print(STORE_NAME)
print(STORE_WEBSITE)
print("-------------------")

print("CHECKOUT AT: " + date_time)

print("-------------------")
print("SELECTED PRODUCTS: ")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("..." + matching_product["name"] + " " + "("+str(to_usd((matching_product["price"])))+")")


        

print("-------------------")

print("SUBTOTAL: " + str(to_usd(total_price)))
tax = float(total_price) * float(TAX_RATE)
print("TAX: " + str(to_usd(tax)))
overall_cost = float(total_price) + float(tax)
print("TOTAL: " + str(to_usd(overall_cost)))
print("-------------------")
print("THANKS, SEE YOU AGAIN SOON!")

######### begin email attempts

#client = SendGridAPIClient(SENGRID_API_KEY)
#print(client, type(client))

#subject = ("Your Receipt from " + str(STORE_NAME) )

#html_content = [
    #html_list_items = "<li>You ordered: " + str(
       # for selected_id in selected_ids:
#            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
 #           matching_product = matching_products[0]
  ##         print("..." + matching_product["name"] + " " + "("+str(to_usd((matching_product["price"])))+")")
        

#html_content = f"""
#<h3>Hello this is your receipt</h3>
#<p>Date: ____________</p>
#<ol>
#   {html_list_items}
#</ol>
#"""
#print(html_content)
#exit()


#print("HTML:", html_content)

# FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
# ... but we can customize the `to_emails` param to send to other addresses
#message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

#try:
#    response = client.send(message)
#
#    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
#    print(response.status_code) #> 202 indicates SUCCESS
#    print(response.body)
#    print(response.headers)

#except Exception as err:
#    print(type(err))
#    print(err)