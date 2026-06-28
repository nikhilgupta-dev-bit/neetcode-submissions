class Solution:
    def jump(self, nums: List[int]) -> int:
        # jump towards the right from index i 
        # jump to i+j
        #incillay we start at nums[0]
        # we need return the minimum no of jumps to reach to the end 
        r=l=0
        #steps=0 # this should be minimum
        res=0
        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r
            r=farthest
            res+=1
        return res 


