from collections import deque 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # idea is multi -bfs 
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        perimeter=0
        # we will push all the cordinbates of land  => 1 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    q.append((i,j))
        while q:
            r,c =q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if not (0<=nr<rows and 0<=nc<cols):
                    perimeter += 1
                elif grid[nr][nc] == 0:
                    perimeter += 1
        return perimeter


            

