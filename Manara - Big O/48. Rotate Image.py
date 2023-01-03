# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:26:24 2023

@author: Nanna
"""

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''cpy = copy.deepcopy(matrix)
        
        for i in range(len(matrix)):
            length = len(matrix)-1
            for j in range(len(matrix)):
                matrix[i][j] = cpy[length][i]
                length -= 1'''

        mat = matrix[:] #copy of matrix list
        i = 0
        for col in zip(*mat): #iterate over the matrix by column/ vertical indices using zip function ==> ex.: col = [1,4,7]
            matrix[i] = list(col)[::-1] #replace the sub-list in matrix with the the reversed col ==> ex.: matrix[0] = [1,2,3] becomes [7,4,1]
            i += 1