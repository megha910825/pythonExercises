# Problem 9: Car Rental Eligibility Scenario:

# A car rental service has specific requirements for renting a car:
# If the customer’s age is less than 18, they cannot rent a car.
# If the customer’s age is between 18 and 25, they can rent but must pay an additional surcharge.
# If the customer’s age is above 25, they can rent with no surcharge.

# Task: Write a program that takes the customer's age as input and prints the rental conditions.

age = int(input("Enter your age::"))
if age < 18:
    print("You cannot rent a car")
elif age > 18 and age < 25 :
    print("You must have to pay additional surcharge")
elif age > 25:
    print("You can rent the car without any surcharge")