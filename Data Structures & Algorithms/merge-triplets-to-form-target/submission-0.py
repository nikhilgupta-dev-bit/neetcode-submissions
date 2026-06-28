class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ai,bi,ci=False,False,False 
        for i in range(0,len(triplets)):
            if triplets[i][0]>target[0] or triplets[i][1]>target[1] or triplets[i][2]>target[2]:
                continue
            if triplets[i][0]==target[0]:
                ai=True 
            if triplets[i][1]==target[1]:
                bi=True 
            if triplets[i][2]==target[2]:
                ci=True 
        return ai and bi and ci
                