"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
import itertools

def days_in_months(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_months = [
            range(31),
            range(29),
            range(31),
            range(30),
            range(31),
            range(30), 
            range(31),
            range(31),
            range(30),
            range(31),
            range(30),
            range(31)
        ]
    else:
        days_in_months = [
            range(31),
            range(28),
            range(31),
            range(30),
            range(31),
            range(30), 
            range(31),
            range(31),
            range(30),
            range(31),
            range(30),
            range(31)
        ]
    return days_in_months

days_in_week = itertools.cycle(('mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun'))

def euler():
    first_mondays = 0
    for year in range(1901, 2001):
        first_mondays += sum(
            1 for day, date in zip(days_in_week, itertools.chain(*days_in_months(year)))
            if day == 'sun' and date == 0
        )
    print(first_mondays)

euler()