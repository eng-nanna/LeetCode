'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''

def singleNumber(nums):
        '''from collections import Counter
        c = Counter(nums)
        for key in c:
            if c[key] == c.most_common()[-1][1]:
                return key'''
        '''for num in nums:
            if nums.count(num) == 1:
                return num'''
        
        '''return min(nums, key=nums.count)'''
        
        res = 0
        for num in nums:
            res = num ^ res
        return res