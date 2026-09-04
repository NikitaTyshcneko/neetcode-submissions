class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
        
        def add_positions(row, column):
            if row > 0: 
                queue.append(row-1, column)
            if row < len(grid):
                queue.append(row+1, column)
            if column > 0:
                queue.append(row, column-1)
            if column < len(grid[0]):
                queue.append(row, column+1)
        
        is_any_rotten = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = 0
        
        while queue:
            length = len(queue)
            is_any_rotten = 0
            for _ in range(length):
                row, column = queue.popleft()
                for dr, dc in directions:
                    i, j = row + dr, column + dc
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and (i,j) not in visited:
                        grid[i][j] = 2
                        queue.append((i, j))
                        visited.add((i, j))
                        is_any_rotten += 1
            if is_any_rotten: result+=1
            print(result)
        print(grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return result
            

        