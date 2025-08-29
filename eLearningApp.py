# You are building an e-learning app for kids . It will ask the user
# to spell the word and it will continue running untill and unless
# user enter the correct spelling of the word ("Hello")
value= "test"
while value != "Hello":
    value = input("Enter the spelling::")
    if (value == 'Hello'):
        break
