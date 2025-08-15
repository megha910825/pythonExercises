# Imagine that you are developer at the ICICI bank. You are developing an application
#which shows the total networth of the customer on the home page.
# Assume that every customer has 5 instruments like:
# Cash balance, Fixed deposit,MF, RD,PPF
## Find out the total net worth

i=0
networth= 0
while i<5:
  value= int(input("Enter the value::"))
  networth = value + networth
  i=i+1
print(networth)