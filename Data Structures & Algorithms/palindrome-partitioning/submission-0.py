class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # the idea is what is a palindrone a string that is same from fronnt and from the back 
        res=[]
        part=[]
        def solve(idx):
            # edge case 
            if idx>=len(s):
                res.append(part.copy())
                return 
            for i in range(idx,len(s)):
                if self.isPalindrone(s,idx,i):
                    # pick 
                    part.append(s[idx:i+1])
                    solve(i+1)
                    # np 
                    part.pop()
        solve(0)
        return res
    def isPalindrone(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False 
            l+=1
            r-=1
        return True 



            # we can include the duplicates => yes 


            