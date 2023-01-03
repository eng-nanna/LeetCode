# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:49:30 2023

@author: Nanna
"""

'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''

def defangIPaddr(address):
    return address.replace(".","[.]")