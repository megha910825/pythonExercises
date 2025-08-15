# Problem 12: Restaurant Discounts
# Scenario: A restaurant offers different discounts based on customer loyalty and the total bill amount:

# If the customer is a loyalty member:
# If the bill is over $100, print "20% discount applied".
# If the bill is between $50 and $100, print "10% discount applied".
# If the bill is below $50, print "5% discount applied".
# If the customer is not a loyalty member:
# If the bill is over $100, print "10% discount applied".
# If the bill is between $50 and $100, print "5% discount applied".
# If the bill is below $50, print "No discount".
# Task: Write a program that takes loyalty status and bill amount as input and prints the discount.

bill_amount = int(input("Enter your bill amount::"))
loyalty_status = input("Enter your loyalty status::")
if loyalty_status == 'yes':
    if bill_amount > 100:
        print("20% discount applied")
    elif bill_amount > 50 and bill_amount < 100:
        print("10% discount applied")
    elif bill_amount < 50:
        print("5% discount applied")
else:
    if bill_amount > 100:
        print("10% discount applied")
    elif bill_amount > 50 and bill_amount < 100:
        print("5% discount applied")
    elif bill_amount < 50:
        print("No discount applied")