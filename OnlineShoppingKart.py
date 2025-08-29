# 1. Online Shopping Cart
# Scenario: You are building a shopping cart for an e-commerce website.

# Task:

# Create a Product class with attributes: name, price, and quantity.
# Create methods to calculate the total cost of a product and to update the quantity.
# Add multiple Product objects to a shopping cart list and calculate the total price of all products in the cart.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def costcalculate(self):
        return int(self.price*self.quantity)
    
p1= Product("toothbrush",20,2)
p2=Product("facecream", 150,3)
shopping_cart=[p1,p2]
total_price=p1.costcalculate() + p2.costcalculate()
print(total_price)
