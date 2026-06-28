class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        used=[False]*n

        def solve(subset):
            if len(subset)==len(nums):
                res.append(subset[:])
            for i in range(n):
                # since we dont want duplicates so once used skip it 
                if used[i]:
                    continue 
                # if not used then add it 
                used[i]=True 
                subset.append(nums[i])
                solve(subset)
                subset.pop()
                used[i]=False 
        solve([])
        return res 

                
