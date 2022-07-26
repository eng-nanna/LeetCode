'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''nlst = []
        total = 0
        while len(nums)>0:
            for i in range(len(nums)):
                total = sum(nums[:i+1])
                nlst.append(total)
                total = 0
            del nums[0]
        max_sum = max(nlst)
        return max_sum
        '''
        maximum = max(nums)
        if maximum < 0:
            return maximum
        max_so_far = 0
        max_end_here = 0
        for e in nums:
            max_end_here += e
            max_end_here = max(max_end_here, 0)
            max_so_far = max(max_so_far,max_end_here)
        return max_so_far
            