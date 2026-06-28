class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows=len(board)
        Cols=len(board[0])
        visited = [[False for _ in range(Cols)] for _ in range(Rows)]
        # what directions can i go top , bottom , left right 
        def solve(r,c,i):
            ## edge case 
            if i==len(word):
                return True 
            if c<0 or r<0 or r>=Rows or c>=Cols or visited[r][c] or word[i]!=board[r][c]:
                return False 
            visited[r][c]=True 
            # if i  go to the top r-1 , c 
            # if i go down then r+1 ,c 
            # if i go to the left r,c-1
            # if i go to the right r,c+1
            ans=(solve(r-1,c,i+1) or solve(r+1,c,i+1) or solve(r,c-1,i+1) or solve(r,c+1,i+1))
            visited[r][c]=False 
            return ans 
        for r in range(Rows):
            for c in range(Cols):
                if solve(r,c,0):
                    return True 
        return False 