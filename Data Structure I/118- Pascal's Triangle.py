'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 1:
            return [[1]]
        for i in range(numRows):
            item = []
            for j in range(i):
                if j == 0:
                    item.append(1)
                else:                
                    x = res[i-1][j-1]+res[i-1][j]
                    item.append(x)
            item.append(1)
            res.append(item)
                
        return res
                
                
                