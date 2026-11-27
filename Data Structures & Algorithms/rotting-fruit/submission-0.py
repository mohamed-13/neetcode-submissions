from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        time = 0
        fresh = 0
        rows,cols = len(grid),len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh>0 and q:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                for dr,dc in directions:
                    ir,ic = r+dr,c+dc
                    if (ir in range(rows) and ic in range(cols)             and grid[ir][ic] == 1):
                        grid[ir][ic] = 2
                        fresh -= 1
                        q.append((ir,ic))

            time +=1
        return time if fresh ==0 else -1