class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_no=bin(n)[2:]
        cnt=0 
        for i in bin_no :
            if i=="1":
                cnt+=1 
        return cnt 