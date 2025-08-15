### hello World
print("Hello World!")

### Grocery Store Discount calculator
def discountCalculator():
  item1=100
  item2=300
  item3=400

  amount=item1+item2+item3
  if ( amount > 500):
     amount= amount*.9
  else:
    amount=amount*.95
  print(amount)

discountCalculator()

## Credit risk calculator
def creditRisk(x,y):
  # loanamount = 100000
  # paidamount = 20000
  # outtsatnding = loanamount-paidamount
  outtsatnding = x-y
  print(outtsatnding)

  if(outtsatnding > 500000):
     print("HIGH RISK!")
  elif(outtsatnding <= 500000):
     print("MODERATE RISK!")
  else:
     print("LOW RISK")

creditRisk(600000,20000)
