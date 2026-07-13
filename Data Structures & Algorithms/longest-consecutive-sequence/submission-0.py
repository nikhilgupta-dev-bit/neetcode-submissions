class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set=set(nums)
        max_length=0 
        for num in hash_set:
            if (num-1) not in hash_set:
                current_num=num
                streak=1 
                while(current_num+1) in hash_set:
                    current_num+=1 
                    streak+=1 
                max_length=max(max_length,streak)
        return max_length
                
