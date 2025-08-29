## print largest number in list

my_list = [30, 20, 10, 50, 60, 70, 80, 90]
largest = my_list[-1]
my_list.append(100)
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)
