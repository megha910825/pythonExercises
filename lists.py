items =["Megha", "Deepak", "Ram","Shyam", "mohan","Sohan"]
listOfIds = [1,2,3,4,5,6]
print(items)
items.append("Mike")
print(len(items))
print(len(listOfIds))
print(items)
removedItem = items.pop(4)
print(removedItem)
print(items)
items[3] = "Mohan new"
print(items)

size = len(items)
i= 0
while i > size:
    print(items[i])
    i = i + 1
temp_item = items[2]
items [2] = items[4]
items[4] = temp_item
print(items)

for i in items:
    print(i)
for i in range(5):
    print(i)
for i in range(1,11,2):
    print(i)