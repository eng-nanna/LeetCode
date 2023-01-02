# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:04:37 2023

@author: Nanna
"""

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    res = []
    
    for num in set1:
        if num in set2:
            res.append(num)
    
    return res