# Problem 13: Smartphone Purchase Eligibility
# Scenario: A store wants to determine if a customer is eligible for purchasing a smartphone on a payment plan:

# If the customer has a credit score above 700:
# If their monthly income is greater than $3,000, print "Eligible for payment plan with 0% interest".
# If their monthly income is between $2,000 and $3,000, print "Eligible for payment plan with 5% interest".
# If the credit score is between 600 and 700:
# Print "Eligible for payment plan with 10% interest".
# If the credit score is below 600:
# Print "Not eligible for a payment plan".
# Task: Write a program that takes the customer's credit score and income as input and prints their eligibility.
credit_score= int(input("Enter your credit score::"))
income = int(input("Enter your income::"))
if credit_score > 700:
    if income > 3000:
        print("Eligible for payment plan with 0% interest")
    elif income < 2000 and income < 3000:
        print("Eligible for payment plan with 5% interest")
elif credit_score > 600 and credit_score < 700:
    print("Eligible for payment plan with 10% interest")
elif credit_score < 600:
    print("Not eligible for a payment plan")
# If the credit score is between 600 and 700: