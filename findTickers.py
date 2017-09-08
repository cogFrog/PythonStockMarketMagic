"""
Code by CodeToad

This short bit of code has one task in mind: find all stocks worth more than $5 dollars.
Why $5? Because my AP Macro teacher has restricted us to buying stocks no cheaper than $5 dollars.
It uses yahoo_finance to check if a stock ticker (the all caps abbreviation) is valid and
matches a stock that matches the price prerequisite. When this is done for all alphabetical
combinations the tickers can be stored in a .txt file for future usage.

"""

from yahoo_finance import Share
import string
import time

# file to add valid tickers to
stockFile = open('stockFile.txt', 'w')

# just keeps track of the start time, so the time taken to process all possibilities can be printed at the end
start = time.time()

#will serve as "root" for each next layer to add new letters onto
list = [""]

# will test alphabetical combinations up to 5 characters long
for x in range(0, 5):
    # for storing values to later become list for the next "layer" of letters
    temp = []
    for e in list:
        for letter in string.ascii_uppercase:
            s = (e + letter)
            temp.append(s)
            price = Share(s).get_price()
            if (price != None and float(price) >= 5.0):
                # makes it clear that it is in fact working
                print(s + ": " + price)
                stockFile.write(s + "\n")
    list = temp

# prints how many seconds it took to complete the task
duration = time.time() - start
print(duration)
