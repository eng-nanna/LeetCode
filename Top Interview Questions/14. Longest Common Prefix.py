'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        maxm = min(strs)
        for i in range(len(maxm)):
            if strs[0] == "":
                return "".join(res)
            else:
                x = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != x:
                    return "".join(res)
            res.append(x)
        
        final = "".join(res)
        return final
    