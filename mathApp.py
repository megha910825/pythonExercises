def addition(x,y):
    z=x+y
    return z
def subtraction(a,b=100):
    c=a-b
    return c

num1=int(input("Enter first number:"))

num2=int(input("Enter second number:"))

print("Addition is ::",addition(num1,num2))
print("subtraction is::",subtraction(num1,num2))
num3=subtraction(30)
print(num3)
def si(p,r,t):
    i=(p*r*t)/100
    return i
interest=si(100000,1,1)
print(interest)

def donation(*amount):
    sum = 0
    for a in amount:
        sum= sum+a
    print(sum)

donation(10,20,30)