## Login Functionality
i= 0
correctPassword = "admin"
while i<3:
    pswd = input("Enter your password:")
    if pswd == 'admin':
        print("login successfully")
        break
    else: 
        if i == 2:
            print("Your password is wrong, Your account is locked")
        else:
            print("Your password is wrong, try again")
    i= i+1