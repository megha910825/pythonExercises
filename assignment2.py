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