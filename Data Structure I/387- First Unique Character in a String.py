'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for x in s:
            freq[x] = freq.get(x,0) + 1
        
        for k,v in freq.items():
            if v == 1:
                return s.index(k)
        return -1
        