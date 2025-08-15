## Portfolio calculator for trading app
##here you asked the user the current holding amount for each share
## you calculate the total worth of the portfolio. or
## ypu calculate the lowest performing stock


## Assume that you are buying a stock and you have to put a stock buy order,
## which is qual to 1% lessa tha the current price of the stock.
## Input: current stock price
## Output: You buy order price
abc = 0
stock_list = []
networth = 0
while abc < 5:
     value = int(input("Enter the stock value::"))
     stock_list.append(value)
     networth = networth + value
     abc = abc + 1
  
print(stock_list)
print(networth)

lowest_share = stock_list[0]
for stock in stock_list:
   if stock < lowest_share:
      lowest_share = stock

print(lowest_share)
## Assume that you are building an AI Agent, now we are writing code for it.
# I first fo and fetch the youube video script , if youtube script contains
## anything vulgur I would take the next step. If no vulgarity in the 
## script I will publish the script as the post on Linkedin automatically.

## A web app . client has asked to develop a functionality called as the Pagination(10 records)
## Input is total number of records
## Output: Total pages


