
# Problem 1: Discount Calculation Scenario:

# A store is offering different discounts based on the purchase amount.
# If the amount is greater than or equal to 5000, the customer gets a 20% discount.
# If the amount is between 2000 and 4999, the customer gets a 10% discount.
# If the amount is between 1000 and 1999, the customer gets a 5% discount.
# If the amount is less than 1000, no discount is given.

# Task: Write a program that takes the purchase amount as input and prints the applicable discount percentage.

purchase_amount = int(input("Enter your purchase amount::"))
discount = 0
if purchase_amount > 5000:
   discount = 20
elif purchase_amount > 2000 and purchase_amount < 5000:
   discount = 10
elif purchase_amount > 1000 and purchase_amount < 2000:
   discount = 5
else:
   discount = 0
print("Your discount percentage::", discount)
# Problem 2: Traffic Light Signal Scenario:

# You are writing a program for a traffic control system.
# If the light is "Red," print "Stop."
# If the light is "Yellow," print "Get ready."
# If the light is "Green," print "Go."

light = input("Enter your light::")
if light == 'Red':
   print("Stop")
elif light == 'Yellow':
   print("Get Ready")
elif light == 'Green':
   print("Go")