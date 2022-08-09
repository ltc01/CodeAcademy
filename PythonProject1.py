# Lovely Loveseat that is the store's namesake.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Price for the loveseat.
lovely_loveseat_price = 254.00

# Inventory with another characteristics piece of furniture!
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inhces wide x 28 inches deep. Black."

# Price of stylish settee.
stylish_settee_price = 180.50

#Luxurious lamps
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Price for luxurious lamp
luxurious_lamp_price = 52.15

#For calculating sales taxes
sales_tax = .088

#expenses of customer's purchasing
customer_one_total = 0

#lists of things customers are purchasing
customer_one_itemization =""

#customer purchased a loveseat
customer_one_total +=lovely_loveseat_price

#updat Items customer purchased
customer_one_itemization+=lovely_loveseat_description

#purchsed a lamp
customer_one_total +=luxurious_lamp_price

#update to list puchased
customer_one_itemization+=luxurious_lamp_description

#calculate sales tax
customer_one_tax = customer_one_total * sales_tax

#Total expense
customer_one_total +=customer_one_tax

#print Receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

