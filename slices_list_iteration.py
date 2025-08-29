my_list = [30, 20, 10, 50, 60, 70, 80, 90]
largest = my_list[-1]

for i in my_list[:-1]:
    print(i)
    if i > largest:
        largest = i

print(largest)