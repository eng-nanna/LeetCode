'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''board_lst = ["1","2","3","4","5","6","7","8","9","."]
        for item in board:
            for i in range(len(item)-1):
                if item[i] not in board_lst:
                        return False
                else:
                    for j in range(i+1,len(item)): 
                        if item[j] != "." and item[i] == item[j] :
                            return False
                        else:
                            continue
        
        for item in range(len(board)-1):
            i = 0
            while i < 9:
                if board[item][i] != "." and board[item][i] == board[item+1][i]:
                    return False
                else:
                    i+=1             
                    
        return True'''
        
        def is_valid(value):
            res=[i for i in value if i!="."]
            return len(res)==len(set(res))
        
        def is_valid_row():
            for row in board:
                if not is_valid(row):
                    return False
            return True
        
        def is_valid_col():
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True
        
        def is_valid_square():
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) 
                                        for y in range(j,j+3)]
                    if not is_valid(square):
                        return False
            return True
        return is_valid_row() and is_valid_col() and is_valid_square()