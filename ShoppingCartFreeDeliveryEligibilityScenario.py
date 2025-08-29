# Problem 10: Shopping Cart Free Delivery Eligibility Scenario:

# An online store provides free delivery only when certain conditions are met:
# If the total order amount is above $100, print "Free delivery".
# If the order amount is between $50 and $100 and the customer is a member, print "Free delivery".
# If the order amount is below $50, print "Delivery charges apply".

# Task: Write a program that takes the total order amount and membership status as input and prints the delivery eligibility.

amount = int(input("enter your total shopping amount::"))
memstatus = input("Are you member of our store::")

if amount > 100:
    print("Free delivery")
elif (amount > 50 and amount < 100):
    if memstatus == 'yes':
       print("Free delivery")
elif amount < 50:
     print("delivery charges apply")