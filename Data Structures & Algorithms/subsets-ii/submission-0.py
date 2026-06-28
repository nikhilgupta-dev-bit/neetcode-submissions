class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # pick and not pick 
        res=[]
        nums.sort()
        n=len(nums)
        def solve(path,idx):
            if idx==n:
                res.append(path[::])
                return 
            # pick that element 
            path.append(nums[idx])
            solve(path,idx+1)
            # not pick the element 
            path.pop()
            # i want a check that my subsets are not same 
            while idx+1<n and nums[idx]==nums[idx+1]:
                idx+=1
            solve(path,idx+1)
        solve([],0)
        return res 


            

