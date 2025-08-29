# Open the file office.py, and complete the code so that the list called stock
# is copied to a new list called assets. Extend the assets list with the items printer 
# and scanner from the list to_order. Then create a list called prices and append the price of each item. 
# To do so, iterate through the assets and check each item's name to add its price with an if/elif block.


# Finally calculate the total amount of assets and print the message in one line: 
# Total stock <all items separated by comma>, total assets: <the sum of prices>$

stock = ['desk', 'chairs', 'computer']
to_order = ['printer', 'scanner']
# Create assets list
assets=stock
# Append printer and scanner to assets
for i in to_order:
   assets.append(i)

desk_price = 100
chairs_price = 300
computer_price = 1200
printer_price = 250
scanner_price = 120

prices = []
# Append each item's price to prices list
for i in assets:
    if i=='desk':
        prices.append(desk_price)
    elif i=='chairs':
        prices.append(chairs_price)
    elif i=='computer':
        prices.append(computer_price)
    elif i=='printer':
        prices.append(printer_price)
    elif i=='scanner':
        prices.append(scanner_price)

total_assets = 0
# Calculate the total amount of prices
for i in prices:
    total_assets += i

# Print the final message with the help of a for loop
print('Total stock:', end=" ")

for i in assets:
    print(i)

print('total assets:', str(total_assets) + "$")
