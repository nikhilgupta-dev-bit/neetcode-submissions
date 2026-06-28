class Solution:
    def longestPalindrome(self, s: str) -> str:
        # this is a pick and not pick concept based 
        # just a  point that we need to check for palindrone 
        res=""
        # base case 
        if len(s)==1:
            return s 
        for i in range(len(s)-1,-1,-1):
            for j in range(0,i+1):
                current_sub=s[j:i+1]
                # now this a palindrone the inner elements should also we a substring 
                if current_sub==current_sub[::-1]:
                    if len(current_sub)>len(res):
                        res=current_sub
        return res 
        