# Open the file data_form.py, and write a function that takes one positional argument and two keyword arguments. 
# The function should ask the user for their full name, birth year, and city of residence. Because the form is for college students in Kerala, 
# India, we should set the birth year and city of residence to the default values 2002 and Kerala.



# Create the data_form function
def data_form(current_year=2024,birth_year=2002,residence="Kerala"):
    full_name=input("Enter your username::")
    birth_year=input("Enter your birth year::") or birth_year
    residence=input("Enter your city of residence::") or residence
    age= current_year -int(birth_year)
    return full_name,age,residence
# Invoke the function with the current year value
print(data_form(current_year=2025))
