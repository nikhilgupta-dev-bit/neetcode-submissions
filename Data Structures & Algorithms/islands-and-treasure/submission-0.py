from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # note : in bfs the queue already sorts the dist in incresing order
        ## multi bfs problem 
        Rows=len(grid)
        Cols=len(grid[0])
        q=deque()
        visited=set()
        # what do we need is dist and node 
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        dist=0 
        # push all the cells with val as 0 
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))
        # the values of cell is inf ko update karna hian and -1 ko skip 
        while q :
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr 
                nc=c+dc 
                if 0<=nr<Rows and 0<=nc<Cols and (nr,nc) not in visited:
                    if grid[nr][nc]==-1 : 
                        # we cannot traverse 
                        continue 
                    visited.add((nr,nc))
                    if grid[nr][nc]==2147483647:
                        grid[nr][nc]=grid[r][c]+1
                        q.append((nr,nc))
        # we dont have to return any thing modify in place 

