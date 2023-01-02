# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:00:18 2023

@author: Nanna
"""

'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
'''
from datetime import datetime
def daysBetweenDates(date1, date2):
    
    d1 = datetime.strtime(date1,"%Y-%m-%d")
    d2 = datetime.strtime(date2,"%Y-%m-%d")
    
    if d1 > d2:
        diff = d1 - d2
    else:
        diff = d2 - d1
        
    return diff.days
