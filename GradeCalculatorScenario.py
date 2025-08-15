# Problem 5: Grade Calculator Scenario:

# A school wants to calculate the grades of students based on their scores.
# If the score is 90 or above, the grade is "A".
# If the score is between 80 and 89, the grade is "B".
# If the score is between 70 and 79, the grade is "C".
# If the score is between 60 and 69, the grade is "D".
# If the score is below 60, the grade is "F".

# Task: Write a program that takes the score as input and prints the grade.
score = int(input("Enter your score::"))
if score > 90:
    grade = "A"
elif score > 80 and score < 90 :
    grade = "B"
elif score > 70 and score < 80 :
    grade = "C"
elif score > 60 and score < 70:
    grade = "D"
elif score < 60:
    grade = "E"
print(grade)