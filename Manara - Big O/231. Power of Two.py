# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:03:48 2023

@author: Nanna
"""

'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1


Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16
'''

def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1 :
        if n%2 != 0:
            return False
        n = n//2
    return True