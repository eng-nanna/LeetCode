'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        temp = []
        count = 0
        for sub_i in mat:
            for i in sub_i:
                temp.append(i)
                count+=1
        if count == r*c:
            i = 0
            for x in range(r):
                item = []
                for y in range(c):
                    item.append(temp[i])
                    i+=1
                res.append(item)

            return res  
        else:
            return mat