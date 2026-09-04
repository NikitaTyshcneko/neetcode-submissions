class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValid(num, row, column):
            for i in range(9):
                if i == column: continue
                if board[row][i] == num:
                    return False
            for i in range(9):
                if i == row: continue
                if board[i][column] == num:
                    return False
            
            start_row = int(row//3)*3
            start_column = int(column//3)*3

            for i in range(3):
                for j in range(3):
                    if start_row+i == row and start_column+j == column:
                        continue
                    if board[start_row+i][start_column+j] == num:
                        return False
            
            return True
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not isValid(board[i][j], i, j):
                        return False
        
        return True
            
            

        