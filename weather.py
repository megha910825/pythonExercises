### Weather app 
# In this user has to provide input of the temperature, if temperature is greater than 40
# it should show HIGH, if temperature is below 10 it should show LOW otherwise show moderate 
# 
temp = int(input("Enter the temperature "))
print(temp)
if temp > 40 :
    print("Temperature is HIGH")
elif temp < 10:
    print("Temperature is LOW ")
else:
    print("moderate temp")