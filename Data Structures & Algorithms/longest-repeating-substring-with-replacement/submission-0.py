class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        hashmap={}
        l=0 
        max_len=0
        count=0
        for r in range(n):
            hashmap[s[r]]=hashmap.get(s[r],0)+ 1
            count=max(count,hashmap[s[r]])
            # shrink kab karna hain 
            if (r-l+1)-count>k:
                hashmap[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len

