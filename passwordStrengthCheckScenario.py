# Problem 7: Nested if for Password Strength Check Scenario:

# A website requires users to create secure passwords.
# If the password length is less than 8 characters, print "Weak password".
# If the password length is 8 or more characters, check:
# If it contains at least one number, print "Strong password".
# Otherwise, print "Moderate password".

# Task: Write a program that checks the strength of a password input.
# Python program showing 
# a use of input()

password = input("Enter your value: ")
if len(password) < 8: 
    print("Weak password")
elif len(password) > 8:
    for i in range(len(password)):
        if password[i].isdigit():
            print("Strong Password")
            break
        


