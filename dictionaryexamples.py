# 9. Tuples & Dictionary - Employee Records (Medium)
# Create a dictionary where each employee ID maps to a tuple containing employee details like (name, age, position).
# Then, allow the user to input an ID to retrieve and display the details of that employee.
# Example: For {"101": ("Alice", 30, "Manager"), "102": ("Bob", 25, "Engineer")}, if the user inputs 
# "101", display ("Alice", 30, "Manager").

employee_details={"101": ("Alice", 30, "Manager"), "102": ("Bob", 25, "Engineer")}
employee_id=input("enter the employee id::")
for key in employee_details.keys():
    if key==employee_id:
        print(employee_details[key])

# 10. Set & Dictionary - Online Course Students (Medium)
# Suppose you are managing student enrollments for two different online courses. 
# Use sets to store the enrolled students' IDs for each course. Display the IDs of students 
# who are enrolled in both courses (intersection of sets).
# Example: For course_A = {1, 2, 3, 4} and course_B = {3, 4, 5, 6}, display Students in both courses: {3, 4}.
course_A = {1, 2, 3, 4}
course_B = {3, 4, 5, 6}
both_courses={}

print(set(course_A).intersection(course_B))

