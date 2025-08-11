items = {"Apple": "Red" , "Watermelon": "Green", "Oranges": "Orange" }
items["Apple"] = "Green"
items["NewApple"] = "Red"
print(items)

for value in items.values():#["Apple", "Watermelon", "Oranges"]
    print(value)

## Assume that you are an app developer for the Amazon . For their 
# retail they want to add two functionality
# 1. Ask the Manager to enter five coupon code and its disocunt
# 2. After finishes the buying we ask the user to enter the coupon code again to give the discount

coupons = {}
i= 0
for  i in range(5):
  code= input("Enter your coupon code::")
  discount = int(input("Enter your discount::"))
  coupons[code] = discount
  i= i+1

print(coupons)

key = input("Enter the coupon code you have ::")
print(coupons[key])
