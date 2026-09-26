class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)-1
        COLS = len(heights[0])-1
        results = set()
        resultsp = set()
        resultsa = set()

        def dfs(row, col, prev, visited):

            if row<0 or row>ROWS or col < 0 or col > COLS or (row, col) in visited or heights[row][col]<prev:
                return False
            
            visited.add((row, col))

            dfs(row+1, col, heights[row][col], visited)
            dfs(row-1, col, heights[row][col], visited)
            dfs(row, col+1, heights[row][col], visited)
            dfs(row, col-1, heights[row][col], visited)

        for c in range(len(heights[0])):
            dfs(0, c, heights[0][c], resultsp)
            dfs(ROWS, c, heights[ROWS][c], resultsa)
        
        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], resultsp)
            dfs(r, COLS, heights[r][COLS], resultsa)

        
        results = resultsp.intersection(resultsa)
        return [[pick[0], pick[1]] for pick in results]
        