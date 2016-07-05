# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isleapyear(year):
    if year%4 == 0:
        if year%100 > 0:
            return True
        else:
            if year%400 == 0:
                return True
            else:
                return False
    else:
        return False

def daysinmonth(month, leap = False):
    if month == 2:
        if leap:
            return 29
        else:
            return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

def dayofmonth(startday = 1, startmonth = 1, startyear = 1900, endyear = 2000):
    day = startday
    month = startmonth
    year = startyear
    dom = 1
    yield dom
    while True:
        leap = isleapyear(year)
        days = daysinmonth(month, leap)
        if dom < days:
            dom += 1
        else:
            month += 1
            dom = 1
            if month == 13:
                month = 1
                year += 1
                if year > endyear:
                    break
        yield dom

def dayofweek(i = 0):
    yield i%7
    while True:
        i += 1
        yield i%7

# Simple counter
first_day = 1
dw = dayofweek(first_day)
dm = dayofmonth(startday = first_day)
counter = 0
dry = 0
# 1900 isn't a leap year, so just run it through 365 times
for i, j in zip(dw, dm):
    if dry == 364:
        print('Breaking after {} days'.format(dry+1))
        print(i, j)
        break
    dry += 1
for i, j in zip(dw, dm):
    if i == 0 and j == 1:
        counter += 1


print('Sundays on First Day: {}'.format(counter))
