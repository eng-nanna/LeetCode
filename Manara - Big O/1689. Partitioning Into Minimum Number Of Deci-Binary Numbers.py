# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:39:34 2023

@author: Nanna
"""
'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9
'''


def minPartitions(self, n: str) -> int:
        '''The largest character in any position in n, 
        will determine how many deci-binary numbers must be added together to obtain n.

        #Example:
        239
        as deci binary only consists of 0s and 1s:
        9 needs nine 1s to be produced
        3 needs three 1s
        2 need double 1s
        '''
        return max(n)