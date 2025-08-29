# Open the file prime_numbers.py, and write a function that checks whether an integer is prime* or not.
# Use a list for the function's argument, and create that list with a for loop for numbers 1 to 20.


# Fun Fact: Prime numbers are used in generating secret keys, e.g in Diffie-Hellman encryption.


# * A number is prime if it is greater than 1 and is divided exactly only by 1 and itself. 
# E.g 4 isn't a prime number, as we can divide it by 1 and 2; 7, however, is a prime number, since we can't divide it exactly with other numbers than 1 and itself.

## Logic
# Inside the function, first check whether each element is greater than 1. If yes, for each item of num_list, perform a range of modulo operands from 2 to the current item's value. 
# Use the range() fucntion for these modulo operations. Append a prime number to prime_numbers if the remainder is not 0, else break.

def prime_numbers(num_list):
      prime_numbers = []
      # Write your code here.
      for num in num_list:
         if num <= 1:
            return num
         else:
            for j in range(2,num):
                  if num%j != 0:
                    # print("prime number",num)
                    prime_numbers.append(num)   
                  break   
      return prime_numbers
    

numbers = []
# Update the list for numbers 2 to 20
for i in range(2,21):
      numbers.append(i)

print("Prime numbers list", prime_numbers(numbers))