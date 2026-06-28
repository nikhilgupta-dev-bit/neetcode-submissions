class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case is if the length is not same then they cant be the anagram 
        if(len(s)!=len(t)):
            return False
        string_1={}
        string_2={}# these are 2 hasmap 
        for i in range(len(s)):
            string_1[s[i]]=1+string_1.get(s[i],0)
            string_2[t[i]]=1+string_2.get(t[i],0)
        return string_1==string_2

        

        