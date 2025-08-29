# Problem 3: Eligibility for Loan Approval Scenario:

# A bank wants to automate loan eligibility checks.
# If a person’s credit score is above 750 and their annual income is greater than 500,000, they are eligible for a loan.
# If their credit score is between 600 and 750 and income is between 300,000 and 500,000, they need a guarantor.
# If their credit score is less than 600, they are not eligible for a loan.

# Task: Write a program that takes credit score and annual income as input and prints the eligibility status.
print("Eligibility for Loan Approval Scenario")
credit_score = int(input("Enter your credit score::"))
annual_income = int(input("Enter your annual income::"))
if credit_score > 750:
    if annual_income > 500000:
       print("You are eligible")
    else:
       print("We need a guranator")
elif (credit_score > 600 and credit_score < 750):
     if (annual_income > 300000 and annual_income < 500000):
        print("We need a guarantor")
     else:
        print("Not eligible")
elif(credit_score < 600):
    print("Not Eligible")
    

