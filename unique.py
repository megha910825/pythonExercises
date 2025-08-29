## Open the file unique.py, and remove any number that is repeated. The final list should have unique numbers.

mixed = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list=[]
#
# Write your code here.
for i in mixed:
    if i not in unique_list:
        unique_list.append(i)

print("The list with unique numbers:")
print(unique_list)