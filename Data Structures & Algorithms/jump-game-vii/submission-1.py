class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        dist=0
        q=deque([0])
        while q:
            i=q.popleft()
            for j in range(max(i+minJump,dist),min(i+maxJump,len(s)-1)+1):
                if s[j]=='0':
                    q.append(j)
                    if j==len(s)-1:
                        return True 
            dist=min(i+maxJump,len(s)-1)+1
        return False 
       
