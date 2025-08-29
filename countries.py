countries = [
       ['Egypt', 'USA', 'India'],
       ['Dubai', 'America', 'Spain'], 
       ['London', 'England', 'France']
    ]
countries2  = [country for row in countries for country in 
                       row if len(country) < 6]
print(countries2)