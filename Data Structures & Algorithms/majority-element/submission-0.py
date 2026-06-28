class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element means the element with the highest count 
        # approch is to maintain a count variable and the store the count and return the max count number 
       nums.sort()
       return nums[len(nums)//2]
        