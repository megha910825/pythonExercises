## Zomato price calculator
## if someone is ordering of total amount more than 500 , you will get 20 % discount
## And if your shipping distance is within 10 km range you will get 5 % extra discount
## On top of that if you are senior citizen with more than 60 years of age you will get more extra
## 5 % discount
## If you are order value is less than 500 and if your age is less than 25 then you get 5 % discount otherwise
## no discount.

order_amount = int(input("Enter your order amount"))
shipping_distance = int(input("Enter your shipping distance"))
discount = int(input("Enter discount"))
# extra_discount = 0
age = int(input("enter your age"))

if order_amount > 500:
    discount = discount + 20
    if shipping_distance < 10 :
       discount = discount + 5
       if(age > 60):
           discount = discount + 5
    else:
      discount = discount + 2
else:
     discount = 10
     if(age < 25):
        discount = discount + 5

amount_to_pay = order_amount - order_amount*(discount/100)
print(amount_to_pay)