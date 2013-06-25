# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# make 12 lists
list = [[]]
for i in range(11):
    list.append([])

start = 2 # 1901-01-01 is a tuesday
count = 0

for year in range(1901,2001):
    for month in range(1,13):
        if month in (9,4,6,11):
            month_length = 30
        elif month == 2:
            month_length = 29 if year%4==0 else 28
        else:
            month_length = 31
        if not start%7: count +=1
        start = start+ month_length

print count