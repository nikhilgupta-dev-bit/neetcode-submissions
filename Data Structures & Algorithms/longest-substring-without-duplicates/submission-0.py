class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hashset=set()
        l=0
        len_of_substring=0
        for r in range(n):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            len_of_substring=max(len_of_substring,r-l+1)
        return len_of_substring
            

            
        