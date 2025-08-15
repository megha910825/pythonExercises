# 1. Tuples - User Profile Storage (Easy)
# Create a tuple to store a user’s profile information: (username, age, city). Then, retrieve and print each element in the tuple.
# Example: For a tuple user_profile = ("Alex", 30, "Mumbai"), print each element separately.
user_profile=("Alex",30,"Mumbai")
print(user_profile)
# 2. List - Task Manager (Easy)
# You are building a simple task manager. Create a list called tasks that stores tasks as strings. 
# Add three tasks to the list and then remove one. Finally, display the remaining tasks.
# Example: Add "Email client", "Review report", "Complete project" to tasks, remove "Review report," and display the list
task_manager=["Email client", "Review report", "Complete project"]
print(task_manager)
task_manager.remove("Review report")
print(task_manager)

# 3. Dictionary - Grocery Price Lookup (Easy)
# Use a dictionary to store grocery items and their prices (e.g., {"Apples": 100, "Milk": 50, "Bread": 30}). 
# Ask the user to input an item name, and then return the price of that item.
# Example: If a user inputs "Milk", display 50.

grocery_price_dict={"Apples": 100, "Milk": 50, "Bread": 30}
item=input("Enter your item name::")
for key in grocery_price_dict.keys():
    if key == item:
       print(grocery_price_dict[key])


# 4. Set - Unique Student List (Easy)
# Create a set called students that stores names of students who have submitted their assignments. 
# Add a few names to the set, including duplicates, and print the final list of unique students.
# Example: Add "John", "Alice", "Bob", "Alice" to the set and display {"John", "Alice", "Bob"}.
students={"John","Alice","Bob","Alice"}
print(students)