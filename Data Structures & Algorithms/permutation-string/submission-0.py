class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1={}
        hashmap2={}
        n=len(s1)
        m=len(s2)
        l=0 
        if n>m:
            return False 
        # case of variable sliding window 
        for c in range(n):
            hashmap1[s1[c]]=hashmap1.get(s1[c],0)+1
        
        for r in range(m):
            hashmap2[s2[r]]=hashmap2.get(s2[r],0)+1
            if r-l+1>n:
                hashmap2[s2[l]]-=1
                if hashmap2[s2[l]]==0:
                    del hashmap2[s2[l]]
                l+=1
            if hashmap1==hashmap2:
                return True 
        return False 


        