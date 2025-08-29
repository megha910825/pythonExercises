## Q1:
## Movie Ticket Pricing
## Scenario: A cinema has different ticket prices based on age.
## Task: Write a program that asks for the customer's age and prints the ticket price.

## Child (0-12): ₹100
## Teen (13-17): ₹150
## Adult (18-59): ₹200
## Senior (60+): ₹120


customer_age = int(input("Enter your age  "))
if customer_age > 0 and customer_age <= 12 :
  price = 100
elif customer_age > 12 and customer_age <= 17 :
  price = 150
elif customer_age > 17 and customer_age <= 59:
  price = 150
elif customer_age > 60:
  price = 120

print(price)


# ## Q2:
# Simple Weather Advisory
# Scenario: A local weather station provides basic weather advisories.
# ## Task: Create a program that takes the current temperature (in Celsius) and provides an appropriate advisory.

# Below 0: "It's freezing! Wear warm layers."
# 0-10: "It's very cold. Wear a heavy jacket."
# 11-20: "It's cool. A light jacket would be good."
# 21-30: "It's pleasant. Enjoy the weather!"
# Above 30: "It's hot. Stay hydrated!"
current_temp = int(input("Enter current temp  "))
if current_temp < 0 :
  print("It's freezing! Wear warm layers.")
elif current_temp > 0 and current_temp <= 10 :
  print("It's very cold. Wear a heavy jacket.")
elif current_temp > 10 and current_temp <= 20:
  print("It's cool. A light jacket would be good.")
elif current_temp > 20 and current_temp <= 30:
  print("It's pleasant. Enjoy the weather!")
elif current_temp > 30:
 print( "It's hot. Stay hydrated!")

# Q3:
# Restaurant Tip Calculator
# Scenario: A restaurant suggests tips based on service quality.
# Task: Write a program that asks for the bill amount and service quality (Excellent, Good, Fair, Poor) and calculates the suggested tip.

# Excellent: 20% tip
# Good: 15% tip
# Fair: 10% tip
# Poor: 5% tip
bill_amount = int(input("Enter bill amount   "))
service_quality = (input("Enter service quality  "))
tip = 0

if service_quality in {"Excellent"}:
  tip = 20/100*bill_amount
elif service_quality in {"Good"} :
  tip = 15/100*bill_amount
elif service_quality in {"Fair"}:
  tip = 10/100*bill_amount
elif service_quality in {"Poor"}:
  tip = 5/100*bill_amount
print(tip)

# Q5:
# Blood Donation Eligibility
# Scenario: A blood donation camp screens donors based on basic criteria.
# Task: Write a program that determines if a person is eligible to donate blood based on:

# Age (must be 18-65)
# Weight (must be above 50 kg)
# Last donation (must be more than 3 months ago)

age = int(input("enter your age : "))
weight = int(input("enter your weight : "))
last_donation = int(input("How many months before you donated blood last?"))

if ( age > 18 and age < 65):
  if(weight > 50):
    if(last_donation > 3):
      print("You are eligible for blood donation")
    else:
      print("Not Eligible")
  else:
    print("Not Eligible")
else:
  print("Not Eligible")

# Q6:
# Simple Car Insurance Premium Estimator
# Scenario: A car insurance company determines premiums based on driver's age and car type.
# Task: Create a program that estimates the premium:

# Age below 25: High risk
# Age 25-40: Medium risk
# Age above 40: Low risk
# Car types: Economy, Sedan, Luxury (increasing premiums in that order)

age = int(input("enter your age : "))
if(age < 25):
  print("High Risk")
elif(age > 25 and age < 40):
  print("Medium Risk")
elif(age>40):
  print("Low Risk")

# Q7:"
# College Admission Predictor
# Scenario: A college has different admission criteria based on exam scores.
# Task: Write a program that predicts admission chances based on exam score:

# Below 60: "Admission unlikely"
# 60-79: "Admission possible"
# 80-89: "Admission probable"
# 90 and above: "Admission assured"

print("College Admission Predictor")
exam_score=int(input("Enter your exam score:"))
if(exam_score < 60):
    print("Admission unlikely")
if(exam_score > 60 and exam_score< 80):
    print("Admission possible")
if(exam_score > 80 and exam_score< 90):
    print("Admission probable")
if(exam_score > 90):
    print("Admission assured")


# Q8:
# Simple Loan Approval System
# Scenario: A bank has basic criteria for loan approval.
# Task: Create a program that determines loan approval based on:

# Credit Score (Good/Fair/Poor)
# Annual Income (Above/Below ₹500,000)
# Employment Status (Employed/Self-employed/Unemployed)

print("Simple Loan Approval System")
credit_score=input("Enter your credit score:")
annual_income=int(input("Enter your annual income:"))
employ_status=input("Enter your Employment status")

if credit_score == 'Good' :
    if(annual_income > 500000):
        if(employ_status == 'Employed'):
           print("Loan Approved")
        else:
            print("Loan Rejected")
    else:
            print("Loan Rejected")
else:
            print("Loan Rejected")
# Q9:
# Mobile Plan Recommender
# Scenario: A telecom company recommends plans based on usage.
# Task: Write a program that suggests a plan based on monthly data usage:

# 0-2 GB: "Basic Plan"
# 2-5 GB: "Standard Plan"
# 5-10 GB: "Heavy User Plan"
# Above 10 GB: "Unlimited Plan"

print("Mobile Plan Recommender")
datausage=int(input("Enter your data usage:"))
if datausage > 0 and datausage < 2:
    print("Basic Plan")
if datausage > 2 and datausage < 5:
    print("Standard Plan")
if datausage > 5 and datausage < 10:
    print("Heavy User Plan")
if datausage > 10:
    print("Unlimited Plan")

# Q10:
# Simple Health Risk Assessment
# Scenario: A health app provides basic risk assessment based on BMI.
# Task: Create a program that calculates BMI (weight in kg / (height in m)^2) and provides a health risk assessment:

# Below 18.5: Underweight"
# 18.5-24.9: "Normal weight"
# 25-29.9: "Overweight"
# 30 and above: "Obese"

print("Simple Health Risk Assessment")
weight=int(input("Enter your weight:"))
if weight < 18.5:
    print("Underweight")
if weight > 18.5 and weight < 25:
    print("Normal weight")
if weight > 25 and weight < 30:
    print("Overweight")
if weight > 30:
    print("Obese")