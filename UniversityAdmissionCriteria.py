# Problem 11: University Admission Criteria
# Scenario: A university has different admission criteria based on the student's grades and extracurricular activities:

# If the student has a grade of 'A':
# If they have participated in extracurricular activities, print "Eligible for scholarship".
# If they have not participated, print "Admitted without scholarship".
# If the student has a grade of 'B':
# If they have participated in extracurricular activities, print "Admitted with standard fee".
# If they have not participated, print "Considered for waitlist".
# If the student has a grade lower than 'B', print "Application not considered".
# Task: Write a program that takes the student’s grade and participation status as input and prints the admission decision.

grade = input("Enter your grade::")
part_status = input("Did you participated in extracurricular activities::")

if grade == 'A':
    if part_status == 'yes':
        print("eligible for scholarship")
    else:
        print("Admitted without scholarship")
elif grade == 'B':
    if part_status == 'yes':
        print("Admitted with standard fee")
    else:
        print("Considered for waiting list")
else:
    print("Application not considered")