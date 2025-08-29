## Question 1: A store sells apples at $5 each and bananas at $3 each. Declare variables apples_price and bananas_price with appropriate values. 
# Calculate the total cost for purchasing 10 apples and 7 bananas and store the result in total_cost.
apples_price = 5
bananas_price = 3

print("Price of 10 apples and 7 bananas")

total_cost = 10*apples_price + 7*bananas_price
print(total_cost)

## Question 2: You have a monthly salary of $4,000 and expenses that include rent ($1,200), groceries ($300), and miscellaneous ($500). 
# Calculate the amount left after expenses and store it in a variable named remaining_balance.
monthly_salary = 4000
rent = 1200
groceries = 300
misc = 500

expenses = rent + groceries + misc
amount_left = monthly_salary - expenses
print(amount_left)

## Question 3: A team won 28 matches this season, and last season they won 18 matches.
#  Declare variables current_season_wins and last_season_wins with respective values. 
# Calculate the increase in matches won and store it in win_difference.
current_season_wins = 28
last_season_wins = 18

win_difference = current_season_wins - last_season_wins
print(win_difference)


## Question 4: A travel company charges $250 per person for a weekend trip and gives a $100 group discount for every 5 people.
#  If a group has 15 people Calculate the total cost for the group and store it in group_trip_cost
group_size = 15
per_person_price = 250
group_discount = 100
valid_group_size_for_discount = 5

total_group_discount = group_size/valid_group_size_for_discount * group_discount
total_cost = per_person_price * group_size
amountToPay= total_cost - total_group_discount
print(amountToPay)

## Question 5: An item costs $120, and there is a discount of 15%.
#  Calculate the final price after the discount and store it in discounted_price.
item_cost = 120
discount = 15
total_discount = 120*15/100
pay_cost = item_cost - total_discount
print(pay_cost)

## Question 6: A company produces 500 units daily and sells each unit for $20. 
# Declare variables units_per_day and price_per_unit.
#  Calculate the monthly revenue assuming a 30-day month and store it in monthly_revenue
units_per_day= 500
price_per_unit = 20
monthly_revenue = 500*20*30
print(monthly_revenue)

##Question 7: A farmer grows wheat on a 150-acre farm and yields 3,000 kg per acre. 
# Declare variables acreage and yield_per_acre.
# Calculate the total wheat production and store it in total_production.

acreage= 150
yield_per_acre= 3000
total_production = acreage*yield_per_acre
print(total_production)

##Question 8: A bakery makes $2 profit on each loaf of bread sold. If they sell 200 loaves in a day, 
# declare variables profit_per_loaf and loaves_sold. 
# Calculate the daily profit and store it in daily_profit
profit_per_loaf = 2
loaves_sold = 200

daily_profit = loaves_sold * profit_per_loaf
print(daily_profit)


###Question 9: You are planning an event for 120 attendees. The venue rental is $800, and catering costs $25 per person. 
# Declare variables venue_cost, catering_cost_per_person, and number_of_attendees. 
# Calculate the total cost of the event and store it in event_total_cost.
number_of_attendees = 120
venue_cost = 800
catering_cost_per_person= 25

event_total_cost = venue_cost + number_of_attendees * catering_cost_per_person
print(event_total_cost)

###Question 10: A school's annual fee per student is $1,500, and they provide a 5% sibling discount. 
# Declare variables annual_fee and sibling_discount_percent. 
# Calculate the discounted fee for one sibling and store it in sibling_discounted_fee.
annual_fee= 1500
sibling_discount_percent=5
discounted_fee = annual_fee - annual_fee*1*sibling_discount_percent/100
print(discounted_fee)

