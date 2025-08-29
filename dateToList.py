def date2list(date):
    datelist = []
    d = " "
    # for loop
    for i  in range(len(date)):
        # Do not add the '-', append d to list and reset var d
        if date[i]=='-':
             datelist.append(d)
             d=''
              # Check if last element of date input
        elif i == len(date)-1: 
            d += date[i]
	       
            datelist.append(d)
        else:
            d+=date[i]
	    
    return datelist

date = input("Enter a date in the format of YYYY-MM-DD: ")
my_list = date2list(date)
print(my_list)
