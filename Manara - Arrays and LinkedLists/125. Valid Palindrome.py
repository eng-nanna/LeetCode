# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:16:09 2023

@author: Nanna
"""

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true

'''

def isPalindrome(s):
    '''res = []
        for chr in s:
            if chr.isalnum():
                res.append(chr.lower())
        rev = list(reversed(res))
        if res == rev:
            return True
        return False'''

    s = ''.join(c for c in s if c.isalnum()) # remove all special characters lise spaces and quotes
    
    return s.lower() == s.lower()[::-1] # compare resulted string to ite reverse but all in lowercase