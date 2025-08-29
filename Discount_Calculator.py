
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
