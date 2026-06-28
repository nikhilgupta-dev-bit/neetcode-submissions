from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=Counter(nums)#{1:1,2:2:3:3} this only stores the count 
        buckets=[[] for _ in range(0,n+1)]#u always create a extra buckets to save the for those whose freq is 0 
        for num,f in freq.items():
            buckets[f].append(num)# this is where the mapping happens 
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if(len(res)==k):
                    return res 
