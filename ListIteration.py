# Open the file iterations.py, and write a program that checks whether a number exists in a list. 
# The program should print Bingo and the number if it exists, and remove this number from the list. 
# The program should exit when all items of the list are gone.


numbers = [1, 2, 3, 4, 5]

while numbers:
    num=int(input("Enter the number::"))
    for i in range(len(numbers)):
        if numbers[i] == num:
           print(num,"Bingo")
           del numbers[i]
           break

print("You found all numbers!")