
# Problem 6: Temperature Classification Scenario: A weather station needs to classify temperature ranges.
# If the temperature is below 0°C, print "Freezing".
# If the temperature is between 0°C and 15°C, print "Cold".
# If the temperature is between 16°C and 30°C, print "Warm".
# If the temperature is above 30°C, print "Hot".

# Task: Write a program that takes the temperature as input and prints the classification.
temp = int(input("Enter the temperature::"))
if temp <= 0 :
    print("Freezing")
elif temp > 0 and temp <= 15 :
    print("Cold")
elif temp >= 16 and temp < 30:
    print("Warm")
elif temp >= 30:
    print("Hot")
