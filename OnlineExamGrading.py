# Problem 16: Online Exam Grading
# Scenario: An online learning platform needs to grade students based on their exam scores and attendance:

# If the score is greater than 90:
# If attendance is above 75%, print "Grade: A".
# If attendance is 75% or less, print "Grade: B".
# If the score is between 70 and 90:
# If attendance is above 75%, print "Grade: B".
# If attendance is 75% or less, print "Grade: C".
# If the score is below 70:
# Print "Grade: D".
# Task: Write a program that takes exam score and attendance as input and prints the grade.

score = int(input("Enter your score::"))
attendance = int(input("Enter your attendance::"))

if score > 90:
    if attendance > 75:
        print("Grade A")
    elif attendance <=75:
        print("Grade B")
elif score > 70 and score < 90:
    if attendance > 75:
        print("Grade B")
    elif attendance <=75:
        print("Grade C")
elif score < 70:
    print("Grade D")
