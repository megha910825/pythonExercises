# 5. Movie Booking System
# Scenario: A theater wants a program to manage movie ticket bookings.

# Task:

# Create a Movie class with attributes: title, available_seats, and ticket_price.
# Add methods to book a ticket (reduce available seats) and calculate total earnings.
# Create multiple movies and allow a user to book tickets for different movies.

class Movie:
    def __init__(self,title,available_seats,ticket_price):
        self.title=title
        self.available_seats=available_seats
        self.ticket_price=ticket_price
        self.total_seats=250
    
    def bookTicket(self):
       self.available_seats=self.available_seats-1
       return(self.available_seats)

    def calculateEarnings(self):
        totalEarnings= 0
        return self.ticket_price*(self.total_seats-self.available_seats)
    
m1=Movie("DDLJ",25,250)
m2=Movie("K3G",22,150)
print(m1.title,m1.bookTicket(),m1.calculateEarnings())
print(m2.title,m2.bookTicket(),m2.calculateEarnings())


# 6. Employee Payroll System
# Scenario: A company wants to automate payroll processing.

# Task:

# Create an Employee class with attributes: name, id, hourly_rate, and hours_worked.
# Add methods to calculate the salary (hourly_rate * hours_worked).
# Implement functionality to update hours_worked for an employee.

class Employee:
    def __init__(self,name,id,hourly_rate,hours_worked):
        self.name=name
        self.id=id
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked

    def calculateSalary(self):
        return(self.hourly_rate*self.hours_worked)
    
    def updatehoursworked(self,hours_worked):
         self.hours_worked=self.hours_worked+hours_worked
         return self.hours_worked

e1=Employee("Deepak",101,150,4)
e2=Employee("Honey",121,80,8)
print(e1.name,e1.calculateSalary(),e1.updatehoursworked(4))
# 7. Smart Home Device Management
# Scenario: You are creating a program to manage smart home devices.

# Task:

# Create a Device class with attributes: name, status (on/off), and power_consumption.
# Add methods to toggle the status and calculate total power consumption if all devices are on.
# Create multiple devices and simulate a smart home setup.

class Device:
    def __init__(self,name,status,power_consumption):
        self.name=name
        self.status=status
        self.power_consumption=power_consumption

    def toggleStatus(self):
        if self.status=="on":
           self.status="off"
        else:
            self.status="on"
        return self.status
    
    def calculateTotalPowerConsumption(self):
        totalPowerConsumption=0
        if self.status=="on":
          totalPowerConsumption=totalPowerConsumption+self.power_consumption
        return totalPowerConsumption
    
d1=Device("DishWasher","on",120)
d2=Device("WaterFilter","off",22)
d3=Device("TV","on",10)

print(d1.name,d1.calculateTotalPowerConsumption())
print(d2.name,d2.calculateTotalPowerConsumption())
print(d3.name,d3.calculateTotalPowerConsumption())
# 8. Online Course Platform
# Scenario: A platform offers multiple courses to students.

# Task:

# Create a Course class with attributes: name, instructor, duration (in hours), and enrolled_students.
# Add methods to enroll a student and display the total number of students enrolled.
# Create multiple courses and simulate student enrollments.

class Course:
    def __init__(self,name,instructor,duration,enrolled_students):
        self.name=name
        self.instructor=instructor
        self.duration=duration
        self.enrolled_students=enrolled_students

    def enrollStudents(self):
        self.enrolled_students=self.enrolled_students+1
        print("total no of enrolled students are::",self.enrolled_students)
        return int(self.enrolled_students)
        
c1=Course("Physics","NVSir",200,45)
c2=Course("Chemistry","VKJSir",200,52)
c3=Course("Maths","BansalSir",200,25)
print(c1.name,c1.enrolled_students,c1.enrollStudents())
print(c2.name,c2.enrolled_students,c2.enrollStudents())
print(c3.name,c3.enrolled_students,c3.enrollStudents())


# 9. Vehicle Service Center
# Scenario: A service center wants to manage its vehicle services.

# Task:

# Create a Vehicle class with attributes: owner_name, vehicle_type, and service_due_date.
# Add methods to update the service_due_date and display the vehicle details.
# Create multiple vehicles and simulate a service schedule.

class Vehicle:
    def __init__(self,owner_name,vehicle_type,service_due_date):
        self.owner_name=owner_name
        self.vehicle_type=vehicle_type
        self.service_due_date=service_due_date
    
    def updateServiceDate(self,new_date):
        self.service_due_date=new_date
        print(self.owner_name,self.vehicle_type,self.service_due_date)
        return self.service_due_date

v1=Vehicle("Scooty","Moped","25-08-2025")
v2=Vehicle("Honda Activa","Scooter","17-08-2025")

print(v1.owner_name,v1.updateServiceDate("21-08-2025"))

# 10. Weather Monitoring System
# Scenario: You are creating a program to track weather conditions in different cities.

# Task:

# Create a CityWeather class with attributes: city_name, temperature, humidity, and condition (e.g., sunny, rainy).
# Add methods to update the weather and display the current conditions for a city.
# Create weather data for multiple cities and implement functionality to search and update weather for a specific city.

class CityWeather:
    def __init__(self,city_name,temperature,humidity,condition):
        self.city_name=city_name
        self.temperature=temperature
        self.humidity=humidity
        self.condition=condition

    def updateWeather(self,new_temp,new_humidity,new_condition):
        self.temperature=new_temp
        self.humidity=new_humidity
        self.condition=new_condition
        return self.temperature,self.humidity,self.condition


cw1= CityWeather("Munich",30,20,"sunny")
cw2=CityWeather("Hamburg",25,50,"windy")
print(cw1.city_name,cw1.updateWeather(25,25,"sunny"),cw1.temperature,cw1.humidity,cw1.condition)