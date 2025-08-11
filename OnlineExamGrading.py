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
    
# Problem 17: Internet Speed Recommendations
# Scenario: A tech support company provides recommendations based on internet speed and user type:

# If the speed is above 100 Mbps:
# If the user is a gamer, print "Optimal speed for gaming and streaming".
# If the user is not a gamer, print "Excellent speed for general usage".
# If the speed is between 50 Mbps and 100 Mbps:
# Print "Good speed for most users".
# If the speed is below 50 Mbps:
# If the user is working from home, print "Consider upgrading for better performance".
# If the user is not working from home, print "Basic speed for minimal use".
# Task: Write a program that takes internet speed and user type as input and prints the recommendation.