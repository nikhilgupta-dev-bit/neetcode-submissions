class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(subset,idx):
            # edge case 
            if idx==len(nums):
                res.append(subset[:])
                return 
            # pick 
            subset.append(nums[idx])
            solve(subset,idx+1)
            # not pick
            subset.pop()
            solve(subset,idx+1)
        solve([],0)
        return res 
