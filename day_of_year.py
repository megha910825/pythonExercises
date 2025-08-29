# Open the file day_of_year.py, and write a function that takes a specific date and the list of monthly days as its arguments. 
# The function returns the corresponding day of the year. E.g 12-04-2020 is day 339 of the year 2020.

# Use the previous leap\_year() function inside the new function to determine if February should be 29 days instead of 28.
#  Also, use the date2list function to convert dates to lists. The code provides the list of monthly days for you.

# Input date should be of the format YYYY-DD-MM.


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

datelist = []
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def date2list(date):
    datelist = []
    d = " "
    for i in range(len(date)):
            if date[i] == "-":
              datelist.append(d)
              d = " "
            elif i == len(date)-1:
              d += date[i]
              datelist.append(d)
            else:
             d += date[i]
    return datelist



def day_in_year(date, days=month_days):
        # Convert the date to a list with the date2list function
        datelist=date2list(date)
        # Create variables for year, month, day
        # from the above list
        year=int(datelist[0])
        month=int(datelist[1])
        day=int(datelist[1])
        print(datelist,year,month,day)
        # Check if year is leap
        is_leap_year=leap_year(year)
        print(is_leap_year)
     
        sum_month_days=0

    # For each month in the month_days list
        for i in range(1, int(month)+1):
           if is_leap_year == True and month_days[i]==28:
               month_days[i]=29
           print(month_days[i])
           sum_month_days = sum_month_days + int(month_days[i])
        # add the previous month's days
        # Note: start from range 1
        sum_month_days = sum_month_days + day

    # Get the last day of the month before the one we entered

        # Return the sum of the previous month plus the current day

        return sum_month_days
date = input("Enter a date in the format of YYYY-MM-DD: ")
d = day_in_year(date, month_days)
print(d)
