# Problem 15: Weather Alert System
# Scenario: A weather alert system needs to send notifications based on temperature and weather conditions:

# If the temperature is above 35°C:
# If it’s sunny, print "Heatwave alert: Stay hydrated and avoid outdoor activities".
# If it’s cloudy, print "Warm weather, stay indoors if possible".
# If the temperature is between 20°C and 35°C:
# Print "Comfortable weather, enjoy your day".
# If the temperature is below 20°C:
# If it’s raining, print "Cold and wet weather, carry an umbrella".
# If it’s not raining, print "Chilly weather, wear warm clothes".
# Task: Write a program that takes temperature and weather condition as input and prints the appropriate alert.

temp = int(input("Enter current temperature:"))
weather_condition= input("Enter weather condition:")

if temp> 35:
    if weather_condition == "sunny":
        print("Heatwave alert: Stay hydrated and avoid outdoor activities")
    elif weather_condition == "cloudy":
        print("Warm weather, stay indoors if possible")
elif temp > 20 and temp < 35:
    print("Comfortable weather, enjoy your day")
elif temp < 20:
    if weather_condition == "raining":
        print("Cold and wet weather, carry an umbrella")
    else:
        print("Chilly weather, wear warm clothes")
