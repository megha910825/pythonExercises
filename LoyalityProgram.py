# Problem 8: Nested if for Loyalty Program Scenario:

# A company runs a loyalty program with different benefits:
# If the user is a "Gold" member:
# If they have been a member for more than 5 years, print "Eligible for VIP access".
# Otherwise, print "Eligible for premium rewards".
# If the user is a "Silver" member:
# Print "Eligible for basic rewards".
# If the user is not a member, print "Not eligible for rewards".

# Task: Write a program that takes membership type and years as input and prints the benefits.

mem_type = input("Enter your membership type::")
no_of_years = int(input("Enter no of years since you are membr of::"))

if mem_type == 'Gold':
    if no_of_years > 5:
        print("Eligible for VIP access")
    else:
        print("Eligible for premium rewards")
elif mem_type == 'Silver':
    print("Eligible for basic rewards")
else:
    print("Not eligible for rewards")