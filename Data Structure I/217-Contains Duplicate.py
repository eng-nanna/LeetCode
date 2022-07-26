'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                        return True
        return False'''
        myset = set(nums)
        if len(nums) == len(myset):
            return False
        else:
            return True