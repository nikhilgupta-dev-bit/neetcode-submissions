class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            bin_no=bin(i)[2:]
            ones=0 
            for i in bin_no:
                if i=="1":
                    ones+=1 
            ans.append(ones)
        return ans 
