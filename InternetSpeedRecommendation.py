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

internet_speed = int(input("Enter your internet speed::"))
user_type= input("Enter user type::")

if internet_speed > 100:
     if user_type== "gamer":
          print("Optimal speed for gaming and streaming")
     else:
          print("Excellent speed for general usage")
elif internet_speed > 50 and internet_speed < 100:
     print("Good speed for most users")
elif internet_speed < 50:
     if user_type=="wfh":
          print("Consider upgrading for better performance")
     else:
        print("Basic speed for minimal use")