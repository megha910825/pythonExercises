# 5. List & Dictionary - Student Grades (Medium)
# Store the names of students and their grades using a dictionary (e.g., {"Alice": [88, 92, 79], "Bob": [78, 85, 88]}). 
# Calculate and print the average grade for each student.
# Example: For {"Alice": [88, 92, 79], "Bob": [78, 85, 88]}, output: Alice: 86.33, Bob: 83.67.

student_grades={"Alice": [88, 92, 79], "Bob": [78, 85, 88]}
for key in student_grades.keys():
    average = 0
    i=0
    for key2 in student_grades[key]:
      average= average+key2
      i=i+1
    average=average/i
    print("Average for student",key,round(average,2))


# 6. Set - Removing Duplicates in a Survey (Medium)
# In a survey, some email addresses were collected multiple times. Use a set to remove 
# duplicate email addresses and display a unique list of all emails.
# Example: From a list emails = ["test@example.com", "admin@example.com", "test@example.com"], 
# output {"test@example.com", "admin@example.com"}.

emails=["test@example.com", "admin@example.com", "test@example.com"]
out_emails=set(emails)
print(out_emails)

# 7. Dictionary - Library Book Collection (Medium)
# Create a dictionary representing a library’s book collection, where keys are book titles and 
# values are the number of copies available. Prompt the user to borrow a book, decrease the count 
# by 1 if available, and display the updated collection.
# Example: For {"Harry Potter": 3, "Python Basics": 2}, if a user borrows "Harry Potter", update to 
# {"Harry Potter": 2, "Python Basics": 2}.


book_collection={"Harry Potter": 3, "Python Basics": 2}
user_input=input("Enter the book you want to borrow::")
for key in book_collection.keys():
   if key==user_input:
      book_collection[key]=book_collection[key]-1
      print(book_collection)

# 8. List - Shopping Cart (Easy to Medium)
# You are building a shopping cart. Create a list of items in the cart and a corresponding list of prices. 
# Calculate the total cost of all items in the cart and display it.
# Example: For items ["Shoes", "Hat", "Shirt"] and prices [500, 150, 300], display Total: 950

items=["Shoes", "Hat", "Shirt"]
prices= [500, 150, 300]
total=0
for key2 in prices:
    total= total+key2


print(total)