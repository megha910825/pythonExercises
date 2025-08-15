# Develop an e commerce app like Amazon and develop "Add to card"
#functionality. Assume your cart hast to have 5 items into it.
total = 0
items = []
for i in range(5):
    print("Enter price of item::", i+1)
    value = int(input())
    items.append(value)
    total = total + value

for item in items:
   print(item)
print(total)