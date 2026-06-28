class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # idea is we have the occurenv in the mpp and increase the count if we get a number that counts is more than one we return it 
        seen=set()
        for num in nums:
            if num in seen:
                return num 
            seen.add(num)
        return -1 


        