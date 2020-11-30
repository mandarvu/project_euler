#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:13:15 2020

@author: mandarupasani

projecteuler.net
problem 19 : Counting Sundays
"""

n_months = [31,
          28,
          31,
          30,
          31,
          30,
          31,
          31,
          30,
          31,
          30,
          31]
lp_months = n_months.copy()
lp_months[1] = 29
days = ["mon",
        "tue",
        "wed",
        "thu",
        "fri",
        "sat",
        "sun"]

def leap_chk(year):
    """1
    A function to check whether a year is leap or not.

    Parameters
    ----------
    year : int
        A year from christ's  birth.

    Returns
    -------
    bool
        True if leap, false otherwise

    Example
    -------
        >>> leap_chk(1996)
            True
        >>> leap_chk(2005)
            False
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

sunday_count = 0
init_day = 'tue'

for year in range(1901,1906):
    # print(init_day)
    if (leap_chk(year)):
        months = lp_months
    else:
        months = n_months

    for i in range(len(months)):
        nxt_day = days[(days.index(init_day) + (months[i] % 7)) % 7]
        # init_day = nxt_day
        if (nxt_day == 'sun'):
            sunday_count += 1

    if (leap_chk(year)):
        init_day = days[(days.index(init_day) + 2) % 7]
    else:
        init_day = days[(days.index(init_day) + 1) % 7]

