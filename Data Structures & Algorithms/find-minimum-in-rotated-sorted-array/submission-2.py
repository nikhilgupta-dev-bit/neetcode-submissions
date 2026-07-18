class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if it is roated then i will get the ans always in right hand side 

        left=0 
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<nums[right]:
                # i will serch in left in side 
                right=mid 
            elif nums[mid]>nums[right]:
                left=mid+1
        return nums[left]