class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## the ways to solve it 
        ## 1. hashmap index,sum 0(n)
        ## 3.two pointers (nlogn)
        mpp={}
        for i,num in enumerate(nums):
            remaining=target-num 
            if remaining in mpp :
                return [mpp[remaining],i]
            mpp[num]=i 