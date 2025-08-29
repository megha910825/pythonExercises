# You are building bankin application
## define a class Account every class should
#have balance account id and account holdee name
# it can wthdraw money and deposit the money

class Banking:
    def __init__(self,account_id,balance,account_holder_name):
      self.account_id = account_id
      self.balance=balance
      self.account_holder_name=account_holder_name
    
    def withdraw(self,amount):
       self.balance=self.balance -amount
       print("Your balance is withdraw", self.balance)
    def deposit(self,amount):
       self.balance=self.balance+amount
       print("Your money is deposited",self.balance)

b1= Banking(1001,20000,"Megha")
b2= Banking(1002,10000,"Shruti")
b1.withdraw(10000)
b1.deposit(2000000)
b2.deposit(1000)
b2.withdraw(200)
nameList= ["Deepak", "Ram","Shyam","Mohan"]
print(nameList[0])
try:
  print(nameList[5])
except:
   print("Exception occured!, Lets continue")
print(nameList[3])
print(nameList[1])
try:
  print(nameList[0])
except NameError:
  print("Forgot to define variable")
except IndexError:
   print("Out of Index exception occured")
except:
   print("Some other error occured")
finally:
   print("executed always")
print("all good now")

item="Foootball"
print(len(item))
print(item.upper())

item2="  Cricket"
item=item+item2
print(item.replace("t","K"))
print("bansal@megha@1991".split("@"))

price=10000
msg=f"My footbal price is {price}"
print(msg)

import datetime
current_date= datetime.datetime.now()
print(current_date)
print(current_date.year)
print(current_date.strftime("%A"))