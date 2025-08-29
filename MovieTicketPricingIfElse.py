
# Problem 4: Movie Ticket Pricing Scenario:

# A cinema offers different ticket prices based on the customer's age.
# If the age is below 5, the ticket is free.
# If the age is between 5 and 12, the ticket price is $5.
# If the age is between 13 and 60, the ticket price is $10.
# If the age is above 60, the ticket price is $7.

# Task: Write a program that takes the age as input and prints the ticket price.

age = int(input("Enter your age::"))
if(age <5):
    ticket_price = 0
elif age > 5 and age < 12:
    ticket_price = 5
elif age > 12 and age < 60:
    ticket_price = 10
elif age > 60:
    ticket_price = 7
print(ticket_price)