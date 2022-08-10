'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)) :
            for num in range(len(matrix[row])):
                if matrix[row][num] > target:
                    return False
                elif matrix[row][num] < target and matrix[row][-1] < target:
                    break
                else:
                    if matrix[row][num] == target:
                        return True
        return False