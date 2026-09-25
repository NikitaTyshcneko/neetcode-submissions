class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        result = []

        def dfs(row, col):
            visited.add((row, col))

            if not word.startswith(''.join(result)): return

            if ''.join(result) == word: return True

            if len(result)>=len(word): return


            if row - 1 > -1 and (row-1, col) not in visited:
                result.append(board[row-1][col])
                if dfs(row-1, col): return True
                result.pop()
                visited.remove((row-1, col))

            if row + 1 < len(board) and (row+1, col) not in visited:
                result.append(board[row+1][col])
                if dfs(row+1, col): return True
                result.pop()
                visited.remove((row+1, col))
            
            if col - 1 > -1 and (row, col-1) not in visited:
                result.append(board[row][col-1])
                if dfs(row, col-1): return True
                result.pop()
                visited.remove((row, col-1))
            
            if col + 1 < len(board[0]) and (row, col+1) not in visited:
                result.append(board[row][col+1])
                if dfs(row, col+1): return True
                result.pop()
                visited.remove((row, col+1))
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    result.append(board[row][col])
                    if dfs(row, col):
                        return True
                    visited.clear()
                    result.pop()
        
        return False
        