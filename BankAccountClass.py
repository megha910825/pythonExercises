# 3. Banking System
# Scenario: You are designing a simple banking application.

# Task:

# Create a BankAccount class with attributes: account_number, holder_name, and balance.
# Add methods to deposit, withdraw, and display balance.
# Ensure withdrawal cannot exceed the balance.

class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount <= self.balance:
           self.balance=self.balance-amount
        else:
            print("Cannot withdrawl,insufficient balance")
    def displaybalance(self):
        return print(self.balance)
    
    
# 4. Student Report Card
# Scenario: A school wants to manage student records.

# Task:

# Create a Student class with attributes: name, roll_number, and a dictionary to store subject-wise marks.
# Add methods to calculate the total and average marks.
# Implement functionality to determine the grade based on the average marks.

class Student:
    def __init__(self,name,roll_number,marks):
        self.name= name
        self.roll_number=roll_number
        self.marks=marks

    def calculateTotalMarks(self):
        total=0
        for key in self.marks.keys():
            total=total+self.marks[key]
        
        return total
    
    def calculateAverageMarks(self):
        counter=0
        totalMarks=0
        for key in self.marks.keys():
            totalMarks=totalMarks+self.marks[key]
            counter= counter+1
        average=round(totalMarks/counter,2)
        return average

s1=Student("Shailu",101,{"maths":100,"english":85,"science":90})

s1=Student("Megha",102,{"maths":95,"english":90,"science":95})
print(s1.name,s1.calculateTotalMarks(),s1.calculateAverageMarks())