# Question 1 from interview cake
#Suppose we could access yesterday's stock prices as a list, where:

#The indices are the time in minutes past trade opening time, which was 9:30am local time.
#The values are the price in dollars of Apple stock at that time.
#So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

#Write an efficient function that takes stock_prices_yesterday and returns the best profit
#I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

import timeit

def get_max_profit(stock_prices_yesterday):

    checkList = []
    counter = 1
    net = 0
    bestProfit = 0
    
    #first loop to get current stock
    for currentStock in stock_prices_yesterday:
        checkList = stock_prices_yesterday[counter:] #creates a smaller list to efficiently loop through again
        for check in checkList: # checks the net profits comparing smaller lists to avoid duplicate checking
            net = check - currentStock
            print (net)
            if net > bestProfit:
                bestProfit = net
        counter = counter + 1

    return bestProfit

stock_prices_yesterday = [10,7,5,8,11,9]

print ("answer: " + str(get_max_profit(stock_prices_yesterday)))
